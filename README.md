#  Quant Trading Journey

**Goal:** Develop quantitative strategies with real alpha and execute them in live trading.

**Current Focus:** Phase 1 - Fundamentals  
**Latest Achievement:** IC analysis + alpha decay for 12‑month momentum  
**Next Milestone:** Cross-sectional momentum strategy backtested

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
Comparison of 5+ fundamental and technical factors using the same IC and alpha‑decay workflow.

---

## 🛠️ Tech Stack

**Python:** pandas, numpy, scipy, statsmodels  
**Data:** yfinance, pandas-datareader  
**Visualization:** matplotlib, seaborn  
**Backtesting:** (coming soon: vectorbt or backtrader)  
**Deployment:** (coming soon: ib_insync for paper trading)

---


## 📁 Project Structure
```
Quant-trading-journey/
├── phase-0/                               # Initial setup + exploration
│ ├── Basic quantitative analysis.ipynb
│ └── Testing quant_utils.ipynb
├── phase-1/                               #  Fundamentals: IC, factors, basic backtests
│ ├── 01_Simple_alpha_factor_and_IC.ipynb
│ └── 02_alpha_decay.ipynb
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

- **Core book:** *Machine Learning for Algorithmic Trading* - Stefan Jansen (Ch 1-8) [file:1]  
- **Supplement:** *Algorithmic Trading* - Ernie Chan (Ch 2, 4, 7) [file:1]

---

## 🚦 Quick Start
Clone repository
git clone https://github.com/ImSeekingAlpha/Quant-trading-journey.git
cd Quant-trading-journey

Install dependencies
pip install -e . # Makes 'quant_utils' importable
pip install -e ".[full]" # Also install every necessary library

Run notebooks
jupyter lab

---

## 📬 Contact

Feedback or collaboration? Open an [Issue](https://github.com/ImSeekingAlpha/Quant-trading-journey/issues) or reach out.

---

**Last updated:** December 2025

