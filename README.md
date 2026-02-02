#  Quant Trading Journey

**Goal:** Develop quantitative strategies with real alpha and execute them in live trading. \
**Current Focus:** Phase 1 - Fundamentals  \
**Latest Achievement:** Momentum 12-1 factor + long-short backtest (Jan 2026) \
**Next Milestone:** Utils update with IC pipelines and factor long-short backtest. 

---

## 📊 Featured Projects

1️⃣ **Simple Alpha Factor & IC**  
Cross-sectional Spearman IC for a 12‑month price momentum factor on an equity universe. Includes IC statistics (mean, median, std, t‑stat) and basic interpretation.

2️⃣ **Alpha Decay of 12‑Month Momentum**  
Extension of the IC pipeline to study how the predictive power of the same factor changes across multiple forward horizons:

- Horizons: 1d, 5d, 10d, 21d, 42d, 126d, 252d  
- Daily IC time series per horizon  
- Summary table (mean, median, std, t‑stat) per horizon  
- Alpha‑decay plot: mean IC vs horizon  
- IC histograms for key horizons (21d, 126d) to inspect the shape of the distribution

3️⃣ **Multi-Factor Comparison**  
Cross-sectional Spearman IC comparison of three fundamental factors (Book-to-Market, Size, ROE) vs 21-day forward returns on aligned universe:  
- Data pipeline: Dual forward-fill for quarterly fundamentals (resample D → reindex price.index → ffill)  
- Universe construction: Index intersection across factors/returns + 30-ticker minimum for IC stability  
- Rank transformation: `.rank(pct=True)` for scale-invariant Uniform[0,1] factors  
- IC metrics: Mean IC, std, T-stat per factor over 978 common trading days (2021-2025)  
- Factor hierarchy: Statistical ranking + economic interpretation (value premium, size effect, quality trap)

4️⃣ **Momentum 12-1 Long-Short Portfolio**
- Canonical 12-1 month momentum factor (Jansen Ch. 3) on S&P 500 universe (2006-2026):
- S&P 500 universe construction: Dollar volume >$1M + 80% coverage → ~400 tickers  
- NaN diagnostics: nan_summary() (Tsay/De Prado) → Leading/internal/trailing decomposition  
- Multi-period geometric returns (1-12m) + 1% winsorization outlier protection  
- IC validation: Spearman rank vs 1m forward returns → IC=0.0113, T-stat=1.09  
- Dollar-neutral portfolio: Equal-weight top/bottom 10% quantile ranks  
- Vectorized backtest: Point-in-time signals (xs(level=1) + shift(1)) → 230 rebalances  
- Performance: Sharpe -0.027, MDD -44.6%, Return -24.3% (validates post-GFC decay)

⏳ **Utils update with IC pipelines (Planned)** \
⏳ **QuantConnect SMA(50,200) + Momentum/MeanRev/Factor (Phase 2 start)**


---

## 🛠️ Tech Stack

**Python:** pandas, numpy, scipy, statsmodels  
**Data:** yfinance, pandas-datareader  
**Visualization:** matplotlib, seaborn  
**Backtesting:** (coming soon: vectorbt or backtrader)  
**Deployment:** (coming soon: ib_insync for paper trading)

---


## 📁 Project Structure
```ruby
Quant-trading-journey/
├── phase-0/                               # Initial setup + exploration
│ ├── Basic quantitative analysis.ipynb
│ └── Testing quant_utils.ipynb
├── phase-1/                               #  Fundamentals: IC, factors, basic backtests
│ ├── 01_Simple_alpha_factor_and_IC.ipynb
│ └── 02_Alpha_decay.ipynb
│ └── 03_Alpha_factor_exploration.ipynb
│ └── 04_Long_short_strategy.ipynb
├── src/quant_utils/                       # Reusable utilities
│ ├── perf.py
│ └── data.py
└── data/ # Downloaded data (not in repo)
```

---

## 🎯 Roadmap Progress

| Phase | Objective | Status |
|-------|-----------|--------|
| **Phase 1**<br>**Fundamentals** | Master Jansen + first backtest | ✅ Complete |
| | Universe construction (liquidity/coverage) | ✅ |
| | IC analysis + factor engineering | ✅ |
| | Momentum 12-1 long-short (Sharpe -0.03) | ✅ |
| **Phase 2**<br>**Rigorous Backtesting** | Multi-factor Sharpe >1.0 | 🟡 Starting |
| | QuantConnect mastery (3 strategies) | ⏳ |
| | 15 original features | ⏳ |
| | XGBoost walk-forward (DD ≤20%) | ⏳ |
| **Phase 3**<br>**Specialization** | Secondary strategy (Stat Arb track) | ⚪ Pending |
| | Cointegration + pairs trading | ⚪ |
| | GARCH volatility models | ⚪ |
| **Phase 4**<br>**Paper → Live** | Live trading €5k-15k | ⚪ Pending |
| | 16 weeks paper trading | ⚪ |

---

## 📚 Main Resources

- **Core book:** *Machine Learning for Algorithmic Trading* - Stefan Jansen (Ch 1-8)

---

## 🚦 Quick Start
Clone repository
```bash
git clone https://github.com/ImSeekingAlpha/Quant-trading-journey.git
cd Quant-trading-journey

Install dependencies
pip install -e .           # Makes 'quant_utils' importable
pip install -e ".[full]"   # Also install every necessary library
```
---

## 📬 Contact

Feedback or collaboration? Open an [Issue](https://github.com/ImSeekingAlpha/Quant-trading-journey/issues) or reach out.

---

Last updated: January 18, 2026

Phase 1 Complete → Phase 2 Next 🚀

