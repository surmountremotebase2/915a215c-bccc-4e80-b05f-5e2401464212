from surmount.base_class import Strategy, TargetAllocation
from surmount.data import ohlcv_data, MarketCap
from pandas import DataFrame

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the ticker symbols for your large-cap investments here
        self.large_cap_tickers = ["AAPL", "MSFT", "GOOGL"]
        # Define or dynamically load your small-cap tickers. Here we just specify placeholders
        self.small_cap_tickers = ["SC1", "SC2", "SC3", "SC4"]  # Placeholder tickers for small-cap companies
        # The proportion of the budget allocated to large caps
        self.large_cap_allocation_portion = 0.048
        # The remainder for small caps
        self.small_cap_allocation_portion = 1 - self.large_cap_allocation_portion

    @property
    def assets(self):
        return self.large_cap_tickers + self.small_cap_tickers

    @property
    def interval(self):
        # Adjust the interval according to your data analysis needs
        return "1day"

    def run(self, data):
        # Initialize allocation dictionary, starting with equal allocation among small caps
        allocation_dict = {ticker: (self.small_cap_allocation_portion / len(self.small_cap_tickers))
                           for ticker in self.small_cap_tickers}
        
        # Allocate the specific portion of the portfolio to large caps evenly
        for ticker in self.large_cap_tickers:
            allocation_dict[ticker] = self.large_cap_allocation_portion / len(self.large_cap_tickers)

        # Here you should define your logic for selecting the "top" small caps based on your criteria.
        # For example, you might use certain technical indicators, market cap size, recent performance, etc.
        # This example does not include specific selection logic due to lack of detailed criteria.

        # Return the allocation dictionary wrapped in a TargetAllocation object
        return TargetAllocation(allocation_dict)