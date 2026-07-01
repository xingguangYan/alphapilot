#!/usr/bin/env python3
"""AkShare Adapter - Deep data via AkShare for AlphaPilot

Usage:
    python akshare_adapter.py kline SYMBOL [PERIOD] [START] [END]
    python akshare_adapter.py financial SYMBOL [TYPE]
    python akshare_adapter.py northbound
    python akshare_adapter.py sector NAME
    python akshare_adapter.py index
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

def kline(symbol, period='daily', start='20240101', end=None):
    ak = _ensure_ak()
    import pandas as pd
    end = end or pd.Timestamp.now().strftime('%Y%m%d')
    df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start, end_date=end, adjust='qfq')
    if df.empty:
        print('[WARN] No data')
        return
    print('Date        Open    High    Low     Close   Vol     Chg%')
    for _, r in df.iterrows():
        print(f'{str(r.iloc[0]):10s} {float(r.iloc[1]):>7.2f} {float(r.iloc[2]):>7.2f} {float(r.iloc[3]):>7.2f} {float(r.iloc[4]):>7.2f} {float(r.iloc[5]):>9.0f} {float(r.iloc[7]):>+6.2f}%')

def financial(symbol, ftype='summary'):
    ak = _ensure_ak()
    try:
        if ftype == 'summary':
            df = ak.stock_financial_abstract(symbol=symbol)
        elif ftype == 'bs':
            df = ak.stock_financial_balance_sheet_by_report_em(symbol=symbol)
        elif ftype == 'pl':
            df = ak.stock_financial_profit_by_report_em(symbol=symbol)
        elif ftype == 'cf':
            df = ak.stock_financial_cash_flow_by_report_em(symbol=symbol)
        else:
            df = ak.stock_financial_abstract(symbol=symbol)
        print(df.head(20).to_string(index=False))
    except Exception as e:
        print(f'[ERROR] {e}')

def northbound():
    ak = _ensure_ak()
    df = ak.stock_hsgt_north_net_flow_in_em(symbol='\u5317\u4e0a')
    print(df.tail(20).to_string(index=False))

def sector(name):
    ak = _ensure_ak()
    df = ak.stock_board_industry_name_em()
    m = df[df['\u677f\u5757\u540d\u79f0'].str.contains(name, na=False)]
    if m.empty:
        print(f'[WARN] No sector: {name}')
        return
    bc = m.iloc[0]['\u677f\u5757\u540d\u79f0']
    print(f'[Sector] {bc}')
    cons = ak.stock_board_industry_cons_em(symbol=bc)
    print(cons.to_string(index=False))

def main():
    p = argparse.ArgumentParser(description='AkShare Adapter')
    sp = p.add_subparsers(dest='cmd')
    k = sp.add_parser('kline')
    k.add_argument('symbol'); k.add_argument('period', nargs='?', default='daily')
    k.add_argument('start', nargs='?', default='20240101')
    k.add_argument('end', nargs='?')
    f = sp.add_parser('financial')
    f.add_argument('symbol'); f.add_argument('ftype', nargs='?', default='summary')
    n = sp.add_parser('northbound')
    s = sp.add_parser('sector'); s.add_argument('name')
    sp.add_parser('index')
    args = p.parse_args()
    if args.cmd == 'kline': kline(args.symbol, args.period, args.start, args.end)
    elif args.cmd == 'financial': financial(args.symbol, args.ftype)
    elif args.cmd == 'northbound': northbound()
    elif args.cmd == 'sector': sector(args.name)
    else: p.print_help()

if __name__ == '__main__':
    main()
