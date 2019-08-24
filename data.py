import pandas as pd
import os
import numpy as np


def get_data_from_csv(symbol_list, csv_dir, start_date, end_date):
    """
        loads desired csv files from symbol_list
        converts to iterator
        returns empty latest_symbol_data, iterator and start and end dates
    """

    symbol_data = {}
    latest_symbol_data = {}
    comb_index = None

    # load files
    for s in symbol_list:
        symbol_data[s] = pd.read_csv(
            os.path.join(csv_dir, "{}.csv".format(s)),
            header=0,
            index_col=0,
            parse_dates=True,
            names=["datetime", "open", "high", "low", "close", "volume", "adj_close"],
        )

        # Combine indexs to match pad values forward if missing
        if comb_index is None:
            comb_index = symbol_data[s].index
        else:
            comb_index.union(symbol_data[s].index)

        latest_symbol_data[s] = []

    # turn into iterator
    for s in symbol_list:
        symbol_data[s] = symbol_data[s].reindex(index=comb_index, method="pad")
        if start_date is not None:
            symbol_data[s] = symbol_data[s].loc[start_date:]
        else:
            start_date = symbol_data[s].index[0]
        if end_date is not None:
            symbol_data[s] = symbol_data[s].loc[:end_date]

        symbol_data[s] = symbol_data[s].iterrows()

    return symbol_data, latest_symbol_data, start_date, end_date


def get_new_bar(symbol, symbol_data):
    for b in symbol_data[symbol]:
        yield b


def update_bars(symbol_list, symbol_data, latest_symbol_data):
    """
        gets new data and appends it to latest_symbol_data
        returns True if finished
    """
    for s in symbol_list:
        try:
            bar = next(get_new_bar(s, symbol_data))
        except StopIteration:
            print("finished back test")
            return True
        else:
            if bar is not None:
                latest_symbol_data[s].append(bar)
    return False


def get_latest_bars(latest_symbol_data, symbol, N=1):
    return latest_symbol_data[symbol][-N:]


def get_bar_values(latest_symbol_data, symbol, key, N=1):
    bars = None
    if N <= len(latest_symbol_data[symbol]):
        bars = np.array([getattr(b[1], key) for b in get_latest_bars(symbol, N)])
    bars = np.nan_to_num(bars)
    return bars


def get_latest_bar_datetime(latest_symbol_data, symbol):
    return latest_symbol_data[symbol][-1][0]
