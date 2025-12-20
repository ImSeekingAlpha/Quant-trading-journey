#  Quant Trading Journey

**Goal:** Develop quantitative strategies with real alpha and execute them in live trading.

**Current Focus:** Phase 1 - Fundamentals  
**Latest Achievement:** Information Coefficient (IC) analysis  
**Next Milestone:** Cross-sectional momentum strategy backtested

---

## 📊 Featured Projects

(In progress).

---

### 2️⃣ Multi-Factor Comparison (In progress)
Comparison of 5+ fundamental and technical factors.

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
├── phase-0/          # Initial setup + exploration
│   ├── Basic quantitative analysis.ipynb
│   └── Testing quant_utils.ipynb
├── phase-1/          # Fundamentals: IC, factors, basic backtests
│   ├── 01_ic_analysis.ipynb
│   └── 02_factor_comparison.ipynb
├── src/quant_utils/  # Reusable utilities
│   ├── perf.py
│   └── data.py
└── data/             # Downloaded data (not in repo)
```

---

## 🎯 Roadmap

| Phase | Objective | Status |
|-------|-----------|--------|
| **Phase 1** | Master factor analysis | 🟡 In progress |
| **Phase 2** | First complete strategy | ⚪ Pending |
| **Phase 3** | 24/7 paper trading | ⚪ Pending |
| **Phase 4** | Diversification + validation | ⚪ Pending |
| **Phase 5** | **Live trading with real capital** | ⚪ Pending |

---

## 📚 Main Resources

- **Core book:** *Machine Learning for Algorithmic Trading* - Stefan Jansen (Ch 1-8)
- **Supplement:** *Algorithmic Trading* - Ernie Chan (Ch 2, 4, 7)

---

## 🚦 Quick Start
```bash
# Clone repository
git clone https://github.com/ImSeekingAlpha/Quant-trading-journey.git
cd Quant-trading-journey

# Install dependencies
pip install -e .                  # Makes 'quant_utils' importable
pip install -e ".[full]"        # Also install every necessary library

# Run notebooks
jupyter lab
```

---

## 📬 Contact

Feedback or collaboration? Open an [Issue](https://github.com/ImSeekingAlpha/Quant-trading-journey/issues) or reach out.

---

**Last updated:** December 2025