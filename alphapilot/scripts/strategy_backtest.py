#!/usr/bin/env python3
"""
Strategy Backtester - Backtesting engine for trading strategies

Usage:
    python strategy_backtest.py ma SYMBOL [SHORT] [LONG]
    python strategy_backtest.py momentum SYMBOL [PERIOD]
    python strategy_backtest.py breakout SYMBOL [PERIOD]
"""
import argparse, sys, math, warnings
warnings.filterwarnings('ignore')

def fetch(symbol, start='20240101', end=None):
    import akshare as ak, pandas as pd
    end = end or pd.Timestamp.now().strftime('%Y%m%d')
    return ak.stock_zh_a_hist(symbol=symbol, period='daily',
                              start_date=start, end_date=end, adjust='qfq')

def run_backtest(df, strategy_name, signals):
    """Common backtest engine"""
    import numpy as np
    df = df.copy()
    df['Signal'] = signals
    df['Position'] = df['Signal'].shift(1).fillna(0)
    df['Return'] = df['收盘'].pct_change()
    df['Strategy'] = df['Position'] * df['Return']
    df = df.dropna()
    if len(df) < 2:
        print('[WARN] Insufficient data for backtest')
        return
    total = (1 + df['Strategy']).prod() - 1
    bh = (1 + df['Return']).prod() - 1
    vol = df['Strategy'].std() * math.sqrt(252)
    sharpe = (df['Strategy'].mean() / df['Strategy'].std() * math.sqrt(252)) if df['Strategy'].std() > 0 else 0
    cum = (1 + df['Strategy']).cumsum()
    dd = (cum.cummax() - cum).max()
    wr = (df['Strategy'] > 0).sum() / max((df['Strategy'] != 0).sum(), 1)
    print(f'\n[{strategy_name}] {df.iloc[0]["\u65e5\u671f"]} - {df.iloc[-1]["\u65e5\u671f"]}')
    print(f'Strategy Return:  {total*100:.2f}%')
    print(f'Buy & Hold:       {bh*100:.2f}%')
    print(f'Excess Return:    {(total-bh)*100:.2f}%')
    print(f'Sharpe Ratio:     {sharpe:.2f}')
    print(f'Max Drawdown:     {dd*100:.2f}%')
    print(f'Win Rate:         {wr*100:.1f}%')
    print(f'Trades:           {(df["Signal"] != df["Signal"].shift(1)).sum()}')

def ma_crossover(symbol, short=20, long=60):
    df = fetch(symbol)
    if df.empty: return
    df['MA_S'] = df['收盘'].rolling(short).mean()
    df['MA_L'] = df['收盘'].rolling(long).mean()
    signals = (df['MA_S'] > df['MA_L']).astype(int) * 2 - 1
    run_backtest(df, f'MA{short}xMA{long} Crossover {symbol}', signals)

def momentum(symbol, period=60):
    df = fetch(symbol)
    if df.empty: return
    mom = df['收盘'].pct_change(period)
    signals = (mom > 0).astype(int) * 2 - 1
    run_backtest(df, f'{period}D Momentum {symbol}', signals)

def breakout(symbol, period=20):
    df = fetch(symbol)
    if df.empty: return
    high = df['最高'].rolling(period).max().shift(1)
    signals = (df['收盘'] > high).astype(int)
    run_backtest(df, f'{period}D Breakout {symbol}', signals)

def main():
    p = argparse.ArgumentParser(description='Strategy Backtester')
    sp = p.add_subparsers(dest='cmd')
    m = sp.add_parser('ma'); m.add_argument('symbol')
    m.add_argument('short', nargs='?', type=int, default=20)
    m.add_argument('long', nargs='?', type=int, default=60)
    mo = sp.add_parser('momentum'); mo.add_argument('symbol')
    mo.add_argument('period', nargs='?', type=int, default=60)
    b = sp.add_parser('breakout'); b.add_argument('symbol')
    b.add_argument('period', nargs='?', type=int, default=20)
    args = p.parse_args()
    if args.cmd == 'ma': ma_crossover(args.symbol, args.short, args.long)
    elif args.cmd == 'momentum': momentum(args.symbol, args.period)
    elif args.cmd == 'breakout': breakout(args.symbol, args.period)
    else: p.print_help()

if __name__ == '__main__':
    main()
