#!/usr/bin/env python3
"""
Market Radar - Multi-timeframe market data aggregator

Usage:
    python market_radar.py realtime SYMBOL
    python market_radar.py kline SYMBOL PERIOD [START] [END]
    python market_radar.py sector SECTOR_NAME
    python market_radar.py capital
    python market_radar.py index CODE
    python market_radar.py breadth
"""
import argparse, sys, warnings
warnings.filterwarnings('ignore')

def _ensure_ak():
    try:
        import akshare as ak
        return ak
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'akshare', '-q'])
        import akshare as ak
        return ak

def realtime(symbol):
    ak = _ensure_ak()
    try:
        df = ak.stock_zh_a_spot_em()
        r = df[df['代码'] == symbol]
        if r.empty:
            df2 = ak.stock_hk_spot_em()
            r = df2[df2['代码'] == symbol]
        if r.empty:
            df3 = ak.stock_us_spot_em()
            r = df3[df3['代码'] == symbol]
        print(r.to_string(index=False) if not r.empty else '[WARN] No data')
    except Exception as e:
        print(f'[ERROR] {e}')

def kline(symbol, period, start, end):
    ak = _ensure_ak()
    import pandas as pd
    end = end or pd.Timestamp.now().strftime('%Y%m%d')
    try:
        df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start, end_date=end, adjust='qfq')
        print(df.to_string(index=False) if not df.empty else '[WARN] No data')
    except Exception as e:
        print(f'[ERROR] {e}')

def sector(name):
    ak = _ensure_ak()
    df = ak.stock_board_industry_name_em()
    matches = df[df['板块名称'].str.contains(name, na=False)]
    if matches.empty:
        print(f'[WARN] No sector: {name}')
        return
    bc = matches.iloc[0]['板块名称']
    print(f'[Sector] {bc}')
    cons = ak.stock_board_industry_cons_em(symbol=bc)
    print(cons.to_string(index=False))

def capital():
    ak = _ensure_ak()
    df = ak.stock_hsgt_north_net_flow_in_em(symbol='北上')
    print(df.tail(20).to_string(index=False))

def market_breadth():
    ak = _ensure_ak()
    df = ak.stock_zh_a_spot_em()
    up = (df['涨跌幅'] > 0).sum()
    down = (df['涨跌幅'] < 0).sum()
    total = len(df)
    print(f'Advancing: {up} ({up/total*100:.1f}%)')
    print(f'Declining: {down} ({down/total*100:.1f}%)')
    print(f'Total:     {total}')
    print(f'AD Ratio:  {up/max(down,1):.2f}')

def main():
    p = argparse.ArgumentParser(description='Market Radar')
    sp = p.add_subparsers(dest='cmd')
    sp.add_parser('realtime').add_argument('symbol')
    k = sp.add_parser('kline')
    k.add_argument('symbol'); k.add_argument('period', nargs='?', default='daily')
    k.add_argument('start', nargs='?', default='20240101'); k.add_argument('end', nargs='?')
    sp.add_parser('capital')
    sp.add_parser('breadth')
    s = sp.add_parser('sector'); s.add_argument('name')
    args = p.parse_args()
    if args.cmd == 'realtime': realtime(args.symbol)
    elif args.cmd == 'kline': kline(args.symbol, args.period, args.start, args.end)
    elif args.cmd == 'capital': capital()
    elif args.cmd == 'breadth': market_breadth()
    elif args.cmd == 'sector': sector(args.name)
    else: p.print_help()

if __name__ == '__main__':
    main()
