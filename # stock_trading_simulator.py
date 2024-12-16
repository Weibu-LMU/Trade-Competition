# stock_trading_simulator.py

import random

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def update_price(self):
        # 随机调整股票价格模拟市场波动
        price_change = random.uniform(-0.05, 0.05) * self.price
        self.price += price_change

    def __str__(self):
        return f"{self.symbol}: ${self.price:.2f}"

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def buy_stock(self, stock, quantity):
        if stock.symbol not in self.stocks:
            self.stocks[stock.symbol] = 0
        self.stocks[stock.symbol] += quantity
        print(f"Purchased {quantity} shares of {stock.symbol} at ${stock.price:.2f} each.")

    def sell_stock(self, stock, quantity):
        if stock.symbol in self.stocks and self.stocks[stock.symbol] >= quantity:
            self.stocks[stock.symbol] -= quantity
            print(f"Sold {quantity} shares of {stock.symbol} at ${stock.price:.2f} each.")
        else:
            print(f"Not enough shares of {stock.symbol} to sell.")

    def get_value(self, stock_data):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            total_value += quantity * stock_data[symbol].price
        return total_value

# 创建一些股票示例
stock_data = {
    "AAPL": Stock("AAPL", 150.00),
    "GOOG": Stock("GOOG", 2800.00),
    "AMZN": Stock("AMZN", 3400.00)
}

# 创建一个投资组合实例
portfolio = Portfolio()

# 模拟购买和出售股票
portfolio.buy_stock(stock_data["AAPL"], 10)
portfolio.sell_stock(stock_data["AAPL"], 5)

# 模拟股票价格波动
for stock in stock_data.values():
    stock.update_price()

# 输出投资组合的当前总价值
print(f"Portfolio Value: ${portfolio.get_value(stock_data):.2f}")
