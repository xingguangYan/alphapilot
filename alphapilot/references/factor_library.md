# Factor Library - Complete Reference

## Factor Definitions

### F1: Value Factors

**PE (Price to Earnings)**
- Calculation: Market Cap / Net Income (TTM)
- Interpretation: Lower = cheaper, but check earnings quality
- Industry adjustment: Compare against sector median
- Score: 1 - (current PE percentile within industry)

**PB (Price to Book)**
- Calculation: Market Cap / Book Value
- Interpretation: Lower = cheaper, best for financials/cyclicals
- Warning: Book value can be misleading for tech/intangibles

**PS (Price to Sales)**
- Calculation: Market Cap / Revenue (TTM)
- Use case: Useful for companies with negative earnings
- Limitation: Ignores profitability differences

**EV/EBITDA**
- Calculation: Enterprise Value / EBITDA
- Enterprise Value = Market Cap + Total Debt - Cash
- Better than PE: Accounts for debt, ignores non-cash charges

**Dividend Yield**
- Calculation: Annual Dividend / Price
- Interpretation: Higher = yield, but check sustainability
- Warning: Yield > 10% may indicate dividend cut risk

### F2: Momentum Factors

**1M Momentum**: (Price_T / Price_T-20) - 1
**3M Momentum**: (Price_T / Price_T-60) - 1  (excl. most recent month)
**6M Momentum**: (Price_T / Price_T-120) - 1  (excl. most recent month)
**12M Momentum**: (Price_T / Price_T-240) - 1  (excl. most recent month)

**RSI (Relative Strength Index)**
- Calculation: RSI = 100 - 100/(1 + RS), RS = Avg Gain / Avg Loss (14 periods)
- Interpretation: >70 overbought, <30 oversold
- Divergence: Price high + RSI lower = bearish divergence

**52W High Proximity**
- Calculation: Current Price / 52W High
- Interpretation: > 0.8 = strong momentum, < 0.5 = weak

### F3: Quality Factors

**ROE (Return on Equity)**
- Calculation: Net Income / Shareholders Equity
- High ROE + Low debt = true quality
- High ROE + High debt = leveraged returns (risky)

**ROA (Return on Assets)**
- Calculation: Net Income / Total Assets
- Independent of capital structure
- Compare within same industry

**Gross Margin Stability**
- Calculation: Std Dev of Gross Margin over 8 quarters
- Lower std dev = more stable, higher quality

**Debt-to-Equity**
- Calculation: Total Liabilities / Shareholders Equity
- Industry dependent: utilities/financials can carry more debt
- > 2.0 for non-financials = high leverage

### F4: Growth Factors

**Revenue Growth (YoY)**
- Current quarter vs same quarter last year
- Organic growth preferred (excl. M&A)

**Earnings Growth (YoY)**
- Net Income growth year over year
- Check for one-time items distorting growth

**Analyst Revision Ratio**
- Calculation: (Upgrades - Downgrades) / Total Ratings
- Positive = improving sentiment
- Leading indicator for price movement

### F5: Low Volatility Factors

**Historical Volatility (60-day)**
- Annualized standard deviation of daily returns
- Low vol stocks tend to outperform on risk-adjusted basis

**Beta (60-day)**
- Covariance(stock, market) / Variance(market)
- Beta < 0.8 = defensive, Beta > 1.2 = aggressive
- Low beta anomaly: low beta stocks often outperform in downturns

### F6: Technical Factors

**MACD**
- MACD Line = EMA(12) - EMA(26)
- Signal Line = EMA(9) of MACD line
- Bullish: MACD crosses above signal
- Bearish: MACD crosses below signal

**Bollinger Bands**
- Middle = SMA(20), Upper = SMA(20) + 2*Std(20), Lower = SMA(20) - 2*Std(20)
- Touch upper band + strong trend = momentum continuation
- Touch upper band + weak trend = mean reversion likely

**Volume Ratio**
- Current Volume / Average Volume (5-day)
- > 2.0 = significant volume (confirmation or reversal)

### F7: Flow Factors

**Northbound Flow Change**
- Change in northbound position over 5/20/60 days
- Sustained buying = foreign institutional confidence

**Block Trade Premium/Discount**
- Block trade price vs market price
- Premium = institutional urgency, Discount = offloading

**Short Interest Ratio**
- Shares Short / Average Daily Volume
- > 10 = high short interest (potential squeeze)

## Industry-Neutral Scoring

For each factor, convert raw value to z-score:
z = (x - mu_industry) / sigma_industry

Then map z-scores to percentile scores (1-100):
- z < -2: score = 5
- -2 <= z < -1: score = 20
- -1 <= z < 0: score = 40
- 0 <= z < 1: score = 60
- 1 <= z < 2: score = 80
- z >= 2: score = 95

## Factor Weight Optimization

To optimize factor weights:
1. Start with a preset (balanced/value/growth/momentum)
2. Run factor regression on past 12 months
3. Identify which factors had highest IC (Information Coefficient)
4. Tilt weights toward high-IC factors
5. Cap individual factor weight at 35%
6. Ensure sum of weights = 100%
