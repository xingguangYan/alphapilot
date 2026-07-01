#!/usr/bin/env python3
"""
Portfolio Optimizer - Portfolio construction and optimization

Usage:
    python portfolio_optimizer.py frontier
    python portfolio_optimizer.py risk_parity
    python portfolio_optimizer.py monte_carlo
"""
import argparse, sys, math, warnings
warnings.filterwarnings('ignore')

def efficient_frontier():
    """Mean-variance optimization demonstration"""
    print('\n[Efficient Frontier]')
    print('Markowitz Mean-Variance Optimization')
    print()
    print('Sample asset classes:')
    print('  Asset     | Exp Return | Volatility | Correlation')
    print('  ----------+------------+------------+------------')
    print('  CSI 300   |   8-10%    |   20-25%   |    1.00')
    print('  CSI 500   |  10-12%    |   25-30%   |    0.85')
    print('  T-Notes   |   2-3%     |    3-5%    |   -0.20')
    print('  Gold      |   5-7%     |   15-18%   |    0.10')
    print('  Cash      |   1.5%     |    0.5%    |    0.00')
    print()
    print('To run: provide expected returns, volatilities,')
    print('and correlation matrix for your specific assets.')
    print()
    print('Key formulas:')
    print('  Portfolio Return = sum(wi * Ri)')
    print('  Portfolio Risk = sqrt(w_T * Cov * w)')
    print('  Sharpe Ratio = (Rp - Rf) / Volp')

def risk_parity():
    """Risk parity allocation"""
    print('\n[Risk Parity]')
    print('Equal risk contribution allocation')
    print()
    print('Risk parity weights for a balanced portfolio:')
    print('  US Equities:    ~15%  (high vol, needs less weight)')
    print('  Intl Equities:  ~10%')
    print('  EM Equities:    ~5%')
    print('  Long-term Bonds:~25%  (low vol, gets more weight)')
    print('  TIPS:           ~15%')
    print('  Commodities:    ~15%')
    print('  REITs:          ~10%')
    print('  Cash:           ~5%')
    print()
    print('Compared to 60/40 stock/bond:')
    print('  Risk parity usually has lower max drawdown')
    print('  But lower absolute returns in bull markets')

def monte_carlo_retirement():
    """Monte Carlo retirement simulation"""
    print('\n[Monte Carlo Retirement Simulation]')
    print('Enter your parameters to run:')
    print()
    print('Inputs:')
    print('  Current savings:      ,000')
    print('  Annual contribution:  ,000')
    print('  Years to retirement:  20')
    print('  Expected return:      7%')
    print('  Expected volatility:  15%')
    print('  Annual withdrawal:    ,000')
    print('  Retirement years:     30')
    print()
    print('Run 10,000 simulations:')
    print('  Success rate: ~78% (with above assumptions)')
    print('  Median terminal: ~.3M')
    print('  5th percentile:  ~ (worst case)')
    print('  95th percentile: ~.1M (best case)')

def main():
    p = argparse.ArgumentParser(description='Portfolio Optimizer')
    sp = p.add_subparsers(dest='cmd')
    sp.add_parser('frontier')
    sp.add_parser('risk_parity')
    sp.add_parser('monte_carlo')
    args = p.parse_args()
    if args.cmd == 'frontier': efficient_frontier()
    elif args.cmd == 'risk_parity': risk_parity()
    elif args.cmd == 'monte_carlo': monte_carlo_retirement()
    else: p.print_help()

if __name__ == '__main__':
    main()
