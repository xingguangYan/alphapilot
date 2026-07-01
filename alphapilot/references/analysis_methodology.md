# Analysis Methodology Reference

## Module 1: Market Radar Checklist

- [ ] Scan 6 timeframes (5min/15min/1H/D/W/M) for trend alignment
- [ ] Check volume confirmation: is price move supported by volume?
- [ ] Calculate advance-decline ratio for market breadth
- [ ] Identify current volatility regime (low/med/high using historical percentiles)
- [ ] Compute rolling 60-day correlation with market index

## Module 2: Fundamental Engine Checklist

- [ ] 3-year revenue CAGR vs industry median
- [ ] Gross margin trend: expanding, stable, or compressing?
- [ ] CFO/NI ratio: above 1.0 = good quality
- [ ] Beneish M-Score threshold check (M < -2.22 = safe)
- [ ] Altman Z-Score check (Z > 2.99 = safe zone)
- [ ] Piotroski F-Score (>=7 = strong)
- [ ] DuPont decomposition: what drives ROE?
- [ ] FCF Yield vs historical and industry
- [ ] ROIC vs WACC: value creation or destruction?

## Module 3: Factor Factory Reference

### Factor Weight Presets

| Style | Value | Momentum | Quality | Growth | Low Vol | Technical | Flow |
|-------|-------|----------|---------|--------|---------|-----------|------|
| Value | 35% | 10% | 20% | 10% | 10% | 10% | 5% |
| Growth | 10% | 15% | 15% | 35% | 5% | 15% | 5% |
| Balanced | 20% | 15% | 20% | 15% | 10% | 10% | 10% |
| Momentum | 10% | 35% | 10% | 10% | 5% | 25% | 5% |
| Defensive | 15% | 5% | 25% | 5% | 30% | 10% | 10% |

### Factor Score Interpretation

| Score Range | Ranking | Interpretation |
|-------------|---------|----------------|
| 80-100 | Top quintile | Strongest factor exposure |
| 60-80 | Above average | Favorable |
| 40-60 | Average | Neutral |
| 20-40 | Below average | Unfavorable |
| 0-20 | Bottom quintile | Weakest exposure |

### Fama-French 5-Factor Model

R_i - R_f = alpha + beta_m*(R_m-R_f) + beta_s*SMB + beta_v*HML + beta_r*RMW + beta_c*CMA + e

- R_m-R_f: Market risk premium (excess return over risk-free)
- SMB: Small Minus Big (size factor)
- HML: High Minus Low (value factor)
- RMW: Robust Minus Weak (profitability factor)
- CMA: Conservative Minus Aggressive (investment factor)

## Module 5: Risk Metrics Reference

### VaR Calculation Methods

| Method | Pros | Cons |
|--------|------|------|
| Historical | No distribution assumption | Limited by data history |
| Parametric | Fast, intuitive | Assumes normal distribution |
| Monte Carlo | Flexible, handles non-linear | Computationally intensive |

### Kelly Criterion

f* = (b*p - q) / b

| Fraction | Behavior | Best For |
|----------|----------|----------|
| Full Kelly (100%) | Maximum growth | High conviction, long track record |
| Half Kelly (50%) | Growth + safety | Most experienced traders |
| Quarter Kelly (25%) | Conservative | New strategies, low conviction |
| 10% Kelly | Very conservative | Systematic risk management |

## Module 6: Portfolio Metrics

### Key Ratios

| Metric | Formula | Target |
|--------|---------|--------|
| Sharpe | (Rp - Rf) / Volp | > 1.0 good, > 2.0 excellent |
| Sortino | (Rp - Rf) / Downside Vol | > 1.5 good |
| Calmar | Annual Return / Max DD | > 1.0 good |
| Information Ratio | Alpha / Tracking Error | > 0.5 good |
| Treynor | (Rp - Rf) / Beta | > market |

## Module 7: Behavioral Bias Quick Reference

| Bias | Definition | Antidote |
|------|------------|----------|
| Confirmation | Seek confirming evidence | Actively seek disconfirming evidence |
| Anchoring | Fixate on reference point | Re-evaluate from first principles |
| Recency | Overweight recent events | Use long-term data and regimes |
| Overconfidence | Overestimate skill | Keep trading journal, track accuracy |
| Loss Aversion | Fear losses > desire gains | Set predetermined stop-losses |
| Herding | Follow the crowd | Contrarian analysis framework |
| Narrative Fallacy | Prefer stories over stats | Demand numerical evidence for claims |

## Module 10: Alert Thresholds

| Alert Type | Condition | Priority |
|------------|-----------|----------|
| Volume spike | Volume > 2x MA(5) | High |
| Volatility jump | Vol > 95th percentile | High |
| Gap move | Gap > 1.5x ATR | Medium |
| Correlation break | Rolling correlation > 0.6 | Medium |
| Insider cluster | 3+ executives selling | High |
| Earnings miss | Actual vs consensus > 2 std | High |
| Technical pattern | Recognized H&S, DBT, etc. | Medium |
| Reg change | ST warning, investigation | Critical |
