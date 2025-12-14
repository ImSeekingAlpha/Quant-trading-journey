# src/quant_utils/perf.py

import pandas as pd
import numpy as np
import yfinance as yf
from typing import Union

def cagr(
    returns: pd.Series | pd.DataFrame, 
    days_per_year: int = 252
) -> float | pd.Series:

    if isinstance(returns, pd.DataFrame):
        if returns.isna().all().any():
            raise ValueError("At least one column is completely empty")
    else:
        if returns.isna().all():
            raise ValueError("The series is empty")

    cum_return = (1 + returns).cumprod().iloc[-1]
    years = len(returns) / days_per_year
    return cum_return ** (1 / years) - 1

def sharpe(
    returns: pd.Series | pd.DataFrame, 
    risk_free: Union[pd.Series, pd.DataFrame, float, None] = None,
    rf_ticker: str = "^IRX",
    days_per_year: int = 252
) -> float | pd.Series:

    if risk_free is None:
        rf_data = yf.download(rf_ticker, period="max", progress=False, auto_adjust=True)
        if rf_data.empty:
            raise ValueError(f"Couldn't get {rf_ticker} data.")
        
        rf_annual = rf_data["Close"] / 100
        rf_daily_values = rf_annual.reindex(returns.index, method="ffill") / days_per_year
        rf_broadcast = rf_daily_values.values  # Array puro → broadcast seguro

    elif isinstance(risk_free, (int, float)):
        rf_broadcast = risk_free / days_per_year
        
    else:
        rf_annual = risk_free.squeeze() if isinstance(risk_free, pd.DataFrame) else risk_free
        rf_daily_values = rf_annual.reindex(returns.index, method="ffill") / days_per_year
        rf_broadcast = rf_daily_values.values

    excess = returns - rf_broadcast

    annual_excess = excess.mean(skipna=True) * days_per_year
    annual_vol = returns.std(skipna=True) * np.sqrt(days_per_year)

    sharpe_ratio = annual_excess / annual_vol
    sharpe_ratio = sharpe_ratio.replace([np.inf, -np.inf], np.nan)

    return sharpe_ratio.round(3)


