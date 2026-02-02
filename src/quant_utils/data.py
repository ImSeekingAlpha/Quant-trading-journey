# utils/data_utils.py

import yfinance as yf
import pandas as pd
import numpy as np
from typing import List, Union, Optional
import os
import itertools

def nan_summary(df):
    """
    Analyze the temporal structure of NaN values per column (ticker),
    with precise separation of leading, internal, and trailing NaNs.
    
    Includes completeness metrics and quality flags, following
    standards from Tsay (2010), De Prado (2018), and Little & Rubin (2002).

    Expects
    -------
    df : pd.DataFrame
        Index = datetime (or time index)
        Columns = tickers (one series per asset)

    Returns
    -------
    pd.DataFrame
        Per-ticker summary with NaN structure, ratios, max gaps,
        and suggested cleaning actions.
    """
    
    def longest_nan_stretch(mask: pd.Series) -> int:
        """Length of longest consecutive NaN sequence."""
        return max(
            (sum(1 for _ in group) for val, group in itertools.groupby(mask) if val),
            default=0
        )

    results = []
    df = df.sort_index()

    for ticker in df.columns:
        series = df[ticker]
        nan_mask = series.isna()

        if not nan_mask.any():
            continue  # Skip tickers with no NaNs

        first_valid = series.first_valid_index()
        last_valid = series.last_valid_index()

        if first_valid is None:
            leading_nans = len(series)
            internal_nans = trailing_nans = 0
        else:
            # Leading: strictly BEFORE first valid
            leading_nans = 0 if first_valid == series.index[0] else series.loc[:first_valid].iloc[:-1].isna().sum()
            # Trailing: strictly AFTER last valid  
            trailing_nans = 0 if last_valid == series.index[-1] else series.loc[last_valid:].iloc[1:].isna().sum()
            # Internal: remainder
            internal_nans = nan_mask.sum() - leading_nans - trailing_nans

        # Max_internal_gap only in VALID region (excludes leading/trailing)
        if first_valid is not None and last_valid is not None:
            internal_region = nan_mask.loc[first_valid:last_valid]
            max_internal_gap = longest_nan_stretch(internal_region)
        else:
            max_internal_gap = 0

        total_nans = int(nan_mask.sum())
        nan_ratio = nan_mask.mean()

        # Action suggestions
        suggestion = []
        if leading_nans > 0 and internal_nans == trailing_nans == 0:
            suggestion.append(f"Trim start at {first_valid.date()}.")
        if trailing_nans > 0 and internal_nans == leading_nans == 0:
            suggestion.append(f"Clip end at {last_valid.date()}.")
        if internal_nans > 0:
            suggestion.append("Internal gaps — forward-fill or interpolate.")
        if total_nans == len(series):
            suggestion.append("All missing — remove ticker.")

        # Quality flag 
        quality = "drop" if total_nans == len(series) else \
                 "drop" if nan_ratio > 0.3 or max_internal_gap > 10 else \
                 "repairable" if total_nans > 0 else "good"

        results.append({
            "ticker": ticker,
            "first_valid_date": first_valid,
            "last_valid_date": last_valid,
            "n_leading_nans": int(leading_nans),
            "n_internal_nans": int(internal_nans),
            "n_trailing_nans": int(trailing_nans),
            "total_nans": total_nans,
            "total_len": len(series),
            "nan_ratio": round(nan_ratio, 4),
            "max_internal_gap": int(max_internal_gap),
            "suggested_action": " ".join(suggestion),
            "quality_flag": quality
        })

    # Handle empty results
    if not results:
        print("No NaNs found in any ticker.")
        return pd.DataFrame()

    summary_df = pd.DataFrame(results).sort_values("nan_ratio", ascending=False)
    summary_df.reset_index(drop=True, inplace=True)
    return summary_df
    
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