# utils/data_utils.py

import yfinance as yf
import pandas as pd
import numpy as np
from typing import List, Union, Optional
import os

def download_data(
    tickers: Union[str, List[str]],
    start: Optional[str] = None,
    end: Optional[str] = None,
    period: Optional[str] = None,        # "1y", "5y", "max", "ytd"...
    interval: str = "1d",
    auto_adjust: bool = True,
    threads: bool = True,
    save_pickle: bool = True,
    pickle_name: Optional[str] = None
) -> pd.DataFrame:

    # Default to max history if nothing specified
    if start is None and end is None and period is None:
        period = "max"

    data = yf.download(
        tickers = tickers,
        start = start,
        end = end,
        period = period,
        interval = interval,
        auto_adjust = auto_adjust,
        threads = threads,
        progress = False
    )
   
    if data.empty:
        raise ValueError(f"No data was found for {tickers}")        
   
    # Extract adjusted close prices
    prices = data['Close'] if isinstance(data.columns, pd.MultiIndex) else data
    if isinstance(prices, pd.DataFrame) and prices.shape[1] == 1:
        prices = prices.iloc[:, 0]  # Return Series for single ticker

    if save_pickle:
        # Get absolute path of this file → go up one level → enter data/
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        data_dir = os.path.join(project_root, "data")
        os.makedirs(data_dir, exist_ok=True)

    if pickle_name is None:
        if len(tickers) <= 10:
            ticker_str = "_".join([t.replace('-','_')[:4] for t in tickers])  
        else:
            ticker_str = f"tickers_{len(tickers)}t"  

        date_str = period or (f"{start[:4]}to{end[:4]}" if start and end else "custom")
        safe_name = f"{ticker_str}_{date_str}_{interval}.pkl"
        pickle_name = os.path.join(data_dir, safe_name)

        full_path = os.path.abspath(pickle_name)
        prices.to_pickle(pickle_name)
        print(f"Saved → {full_path}")

    return prices

def load_data(path: str) -> pd.DataFrame:
    return pd.read_pickle(path)