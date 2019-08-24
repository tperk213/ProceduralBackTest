"""
    Goal
        Build a back test platform that is procedural and easy to understand

    The program will be built around data and functions to manipulate the data
    Data
        - latest_data
        - data_generator
        
        - Portfolio
            - cur_holdings
            - cur_positions
            - total_value

        - que of priority 1 signals
        - que of priority 2 signals

    Functions
        
        - 

    pseudo code

    Setup
        Load data from csv files into data frame
        convert dataframe into itterator
        get first data_point from itterator
        set latest_data to first point
        set cur_capital
        set cur_positions to 0
        set total value to cur_capital
    
    loop until itterator finished
        get next data point from itterator
        add it to latest data
        get signals and add to ques

        Handle signals
        loop
            priority 1 signals
            adjust positions and capital according to signals

        loop
            priority 2 signals
            adjust positions and capital according to signals

    calculate stats
    display results
    save results
"""

import numpy as np


from math import isnan
from portfolio import Portfolio
import data
import queue

symbol_list = []
csv_dir = ""
start_date = None
end_date = None
starting_capital = 100000

symbol_data, latest_symbol_data, start_date, end_date = data.get_data_from_csv(
    symbol_list, csv_dir, start_date, end_date
)

pf = Portfolio(symbol_list, starting_capital, start_date)

priority_1_signals = queue.Queue()
priority_2_signals = queue.Queue()

data.update_bars(symbol_list, symbol_data, latest_symbol_data)

count = 0
while True:
    count += 1

    if data.update_bars(symbol_list, symbol_data, latest_symbol_data) == True:
        break

    calculate_signal(latest_symbol_data, symbol_list)


def calculate_signal(latest_symbol_data, symbol_list, eom_strat):
    """
            if its the start of the month sell everything and rebuy everything
    """
    bar_date = data.get_latest_bar_datetime(symbol_list[0])
    ######################################################################
    if self._start_of_month(bar_date):
        for symbol in self.tickers_invested:
            signal = SignalEvent(symbol, bar_date, "EXIT", 1)
            self.events.put(signal)
        for symbol in self.symbol_list:
            """
                Check to see if the adj_close isn't nan
            """
            if not numpy.isnan(self.data.get_bar_value(symbol, "adj_close")):
                signal = SignalEvent(symbol, bar_date, "BUY", "BALANCE")
                self.events.put(signal)
