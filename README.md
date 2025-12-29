#  Quant Trading Journey

**Goal:** Develop quantitative strategies with real alpha and execute them in live trading. \
**Current Focus:** Phase 1 - Fundamentals  \
**Latest Achievement:** Multi-factor analysis \
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

3️⃣ **Multi-Factor Comparison (Planned)**  
Cross-sectional Spearman IC comparison of three fundamental factors (Book-to-Market, Size, ROE) vs 21-day forward returns on aligned universe:  
- Data pipeline: Dual forward-fill for quarterly fundamentals (resample D → reindex price.index → ffill)  
- Universe construction: Index intersection across factors/returns + 30-ticker minimum for IC stability  
- Rank transformation: `.rank(pct=True)` for scale-invariant Uniform[0,1] factors  
- IC metrics: Mean IC, std, T-stat per factor over 978 common trading days (2021-2025)  
- Factor hierarchy: Statistical ranking + economic interpretation (value premium, size effect, quality trap)

⏳  **Utils update with IC pipelines (Planned)**\
⏳  **Factor Long-Short (Planned)**

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
├── src/quant_utils/                       # Reusable utilities
│ ├── perf.py
│ └── data.py
└── data/ # Downloaded data (not in repo)
```

---

## 🎯 Roadmap

| Phase      | Objective                       | Status        |
|-----------|---------------------------------|---------------|
| **Phase 1** | Master factor analysis          | 🟡 In progress |
| **Phase 2** | First complete strategy         | ⚪ Pending     |
| **Phase 3** | 24/7 paper trading              | ⚪ Pending     |
| **Phase 4** | Diversification + validation    | ⚪ Pending     |
| **Phase 5** | **Live trading with real capital** | ⚪ Pending |

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

**Last updated:** December 2025

