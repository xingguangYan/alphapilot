#!/usr/bin/env python3
"""
Risk Assessment - VaR, stress testing, and position sizing

Usage:
    python risk_assessment.py var SYMBOL [METHOD] [CONFIDENCE]
    python risk_assessment.py stress SYMBOL SCENARIO
    python risk_assessment.py kelly WIN_RATE AVG_WIN AVG_LOSS [FRACTION]
"""
import argparse, sys, math, warnings, random
warnings.filterwarnings('ignore')

def calc_var(symbol, method='historical', confidence=0.95):
    """Calculate Value at Risk"""
    print(f'\n[VaR Analysis] {symbol} | Method: {method.upper()} | Conf: {confidence:.0%}')
    try:
        import akshare as ak
        import pandas as pd
        import numpy as np
        df = ak.stock_zh_a_hist(symbol=symbol, period='daily',
                                start_date='20240101', adjust='qfq')
        returns = df['收盘'].pct_change().dropna().values
        if method == 'historical':
            var = np.percentile(returns, (1-confidence)*100)
        elif method == 'parametric':
            mu = np.mean(returns); sigma = np.std(returns)
            from scipy.stats import norm
            var = norm.ppf(1-confidence, mu, sigma)
        elif method == 'monte_carlo':
            mu = np.mean(returns); sigma = np.std(returns)
            sims = np.random.normal(mu, sigma, 10000)
            var = np.percentile(sims, (1-confidence)*100)
        else:
            var = np.percentile(returns, (1-confidence)*100)
        cvar = returns[returns <= var].mean() if len(returns[returns <= var]) > 0 else var
        print(f'  VaR({confidence:.0%}): {var*100:.2f}%')
        print(f'  CVaR:              {cvar*100:.2f}%')
        print(f'  Daily volatility:  {np.std(returns)*100:.2f}%')
        print(f'  Annual vol:        {np.std(returns)*math.sqrt(252)*100:.2f}%')
        print(f'  Max drawdown (YTD): {np.min(np.minimum.accumulate(1+returns)-1)*100:.2f}%')
    except Exception as e:
        print(f'[ERROR] {e}')

def stress_test(symbol, scenario='2008'):
    """Scenario stress testing"""
    scenarios = {
        '2008': {'name': '2008 Financial Crisis', 'impact': -0.50,
                 'desc': 'Global financial meltdown, Lehman collapse'},
        '2015': {'name': '2015 China Crash', 'impact': -0.30,
                 'desc': 'Chinese stock market crash, margin call cascade'},
        '2020': {'name': '2020 COVID Shock', 'impact': -0.25,
                 'desc': 'Global pandemic, economic shutdown'},
        '2022': {'name': '2022 Rate Hike', 'impact': -0.20,
                 'desc': 'Aggressive Fed rate hikes, tech selloff'},
    }
    s = scenarios.get(scenario, list(scenarios.values())[0])
    print(f'\n[Stress Test] {symbol}')
    print(f'Scenario: {s["name"]}')
    print(f'Description: {s["desc"]}')
    print(f'Estimated impact: {s["impact"]*100:.0f}%')
    print()
    print(f'If invested ,000:')
    print(f'  Portfolio would decline to ')
    print(f'  Loss amount: ')
    print()
    print('Recovery time:')
    if scenario == '2008':
        print('  ~3-5 years for broad recovery')
    elif scenario == '2015':
        print('  ~2-3 years for small/mid caps')
    elif scenario == '2020':
        print('  ~6-12 months (V-shaped recovery)')
    elif scenario == '2022':
        print('  ~1-2 years depending on sector')

def kelly_criterion(win_rate, avg_win, avg_loss, fraction=1.0):
    """Kelly Criterion position sizing"""
    print(f'\n[Kelly Criterion]')
    b = avg_win / abs(avg_loss)  # win/loss ratio
    p = win_rate
    q = 1 - p
    kelly_pct = (b * p - q) / b
    print(f'  Win rate:       {p:.1%}')
    print(f'  Avg win/loss:   {b:.2f}x')
    print(f'  Full Kelly:     {kelly_pct*100:.1f}% of capital')
    print(f'  1/2 Kelly:      {kelly_pct*0.5*100:.1f}% of capital')
    print(f'  1/4 Kelly:      {kelly_pct*0.25*100:.1f}% of capital')
    if kelly_pct > 0.3:
        print(f'  [!] Full Kelly >30% suggests high confidence')
    if kelly_pct < 0:
        print(f'  [!] Negative Kelly - edge not found, avoid trade')

def main():
    p = argparse.ArgumentParser(description='Risk Assessment Tool')
    sp = p.add_subparsers(dest='cmd')
    v = sp.add_parser('var')
    v.add_argument('symbol'); v.add_argument('method', nargs='?', default='historical')
    v.add_argument('confidence', nargs='?', type=float, default=0.95)
    s = sp.add_parser('stress')
    s.add_argument('symbol'); s.add_argument('scenario', nargs='?', default='2008')
    k = sp.add_parser('kelly')
    k.add_argument('win_rate', type=float); k.add_argument('avg_win', type=float)
    k.add_argument('avg_loss', type=float); k.add_argument('fraction', nargs='?', type=float, default=1.0)
    args = p.parse_args()
    if args.cmd == 'var': calc_var(args.symbol, args.method, args.confidence)
    elif args.cmd == 'stress': stress_test(args.symbol, args.scenario)
    elif args.cmd == 'kelly': kelly_criterion(args.win_rate, args.avg_win, args.avg_loss, args.fraction)
    else: p.print_help()

if __name__ == '__main__':
    main()
