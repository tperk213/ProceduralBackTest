class Portfolio:
    def __init__(self, symbol_list, starting_capital, start_date):
        self.cur_positions, self.cur_holdings = self.construct_holdings_positions(
            symbol_list, starting_capital, start_date
        )

    def construct_holdings_positions(self, symbol_list, starting_capital, start_date):
        cur_positions = dict((k, v) for k, v in [(s, 0) for s in symbol_list])
        cur_positions["datetime"] = start_date
        cur_positions = [cur_positions]

        cur_holdings = dict((k, v) for k, v in [(s, 0) for s in symbol_list])
        cur_holdings["datetime"] = start_date
        cur_holdings["cash"] = starting_capital
        cur_holdings["total"] = starting_capital
        cur_holdings = [cur_holdings]

        return cur_positions, cur_holdings
