#!/usr/bin/env python3
"""
Fundamental Analyzer - Financial statement analysis and quality scoring

Usage:
    python fundamental_analyzer.py mscores SYMBOL
    python fundamental_analyzer.py zscore SYMBOL
    python fundamental_analyzer.py fscore SYMBOL
    python fundamental_analyzer.py dupont SYMBOL
    python fundamental_analyzer.py fcf SYMBOL
"""
import argparse, sys, math, warnings
warnings.filterwarnings('ignore')

def fetch_financials(symbol):
    try:
        import akshare as ak
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'akshare', '-q'])
        import akshare as ak
    bs = ak.stock_financial_balance_sheet_by_report_em(symbol=symbol)
    pl = ak.stock_financial_profit_by_report_em(symbol=symbol)
    cf = ak.stock_financial_cash_flow_by_report_em(symbol=symbol)
    return bs, pl, cf

def calc_mscore(symbol):
    """Beneish M-Score - earnings manipulation detection"""
    print(f'\n[Beneish M-Score] {symbol}')
    print('M-Score = -4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI')
    print('         + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI')
    print()
    print('Threshold: M > -1.78  -> likely manipulator')
    print('           M < -2.22  -> unlikely manipulator')
    print()
    print('[NOTE] Full calculation requires detailed financial data.')
    print('For a quick estimate, examine:')
    print('  1. Revenue growth vs receivable growth (DSRI)')
    print('  2. Gross margin trend (GMI)')
    print('  3. Asset quality changes (AQI)')
    print('  4. Sales growth sustainability (SGI)')
    print('  5. Total accruals to total assets (TATA)')

def calc_zscore(symbol):
    """Altman Z-Score - bankruptcy risk"""
    print(f'\n[Altman Z-Score] {symbol}')
    print('Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5')
    print('X1 = Working Capital / Total Assets')
    print('X2 = Retained Earnings / Total Assets')
    print('X3 = EBIT / Total Assets')
    print('X4 = Market Value of Equity / Total Liabilities')
    print('X5 = Sales / Total Assets')
    print()
    print('Thresholds:')
    print('  Z > 2.99 -> Safe zone')
    print('  1.81 < Z < 2.99 -> Grey zone')
    print('  Z < 1.81 -> Distress zone')

def calc_fscore(symbol):
    """Piotroski F-Score - value quality"""
    print(f'\n[Piotroski F-Score] {symbol}')
    print('9 criteria (0/1 each, max score=9):')
    print('  Profitability: Positive ROA (1), Positive CFO (2),')
    print('    ROA increase (3), CFO > ROA (4)')
    print('  Leverage/Liquidity: Leverage decrease (5),')
    print('    Liquidity increase (6), No equity dilution (7)')
    print('  Operating Efficiency: Gross margin increase (8),')
    print('    Asset turnover increase (9)')
    print()
    print('F-Score >= 7 -> Strong value')
    print('F-Score <= 3 -> Weak fundamentals')

def dupont(symbol):
    """DuPont decomposition"""
    print(f'\n[DuPont Decomposition] {symbol}')
    print('ROE = Net Profit Margin x Asset Turnover x Equity Multiplier')
    print()
    print('Net Profit Margin = Net Income / Revenue')
    print('  -> Measures cost control & pricing power')
    print('Asset Turnover = Revenue / Total Assets')
    print('  -> Measures operational efficiency')
    print('Equity Multiplier = Total Assets / Equity')
    print('  -> Measures financial leverage')
    print()
    print('Interpretation:')
    print('  High NPM + Low Turnover = Luxury/brand-driven model')
    print('  Low NPM + High Turnover = Volume-driven model')
    print('  High Multiplier = Heavy leverage, higher risk')

def fcf_analysis(symbol):
    """Free cash flow analysis"""
    print(f'\n[FCF Analysis] {symbol}')
    print('FCF = Operating Cash Flow - CapEx')
    print('FCF Yield = FCF / Market Cap')
    print()
    print('Interpretation:')
    print('  FCF Yield > 5%  -> Potential value (check sustainability)')
    print('  FCF Yield > 10% -> Deep value (verify one-time items)')
    print('  FCF Yield < 0   -> Burning cash (need financing)')
    print()
    print('CFO / NI Ratio:')
    print('  > 1.0 -> Good earnings quality')
    print('  0.5-1.0 -> Moderate quality')
    print('  < 0.5 -> Potential red flag (accrual-heavy earnings)')

def main():
    p = argparse.ArgumentParser(description='Fundamental Analyzer')
    sp = p.add_subparsers(dest='cmd')
    for c in ['mscores','zscore','fscore','dupont','fcf']:
        sp.add_parser(c).add_argument('symbol')
    args = p.parse_args()
    if args.cmd == 'mscores': calc_mscore(args.symbol)
    elif args.cmd == 'zscore': calc_zscore(args.symbol)
    elif args.cmd == 'fscore': calc_fscore(args.symbol)
    elif args.cmd == 'dupont': dupont(args.symbol)
    elif args.cmd == 'fcf': fcf_analysis(args.symbol)
    else: p.print_help()

if __name__ == '__main__':
    main()
