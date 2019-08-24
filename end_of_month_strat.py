class End_of_month_rebalance:
    def __init__(self, start_date, symbol_list):
        self.previous_date = start_date
        self.invested_in = {symbol: False for symbol in symbol_list}

