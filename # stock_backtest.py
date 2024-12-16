# stock_backtest.py

import pandas as pd
import matplotlib.pyplot as plt

# 读取股票历史数据
stock_data = pd.read_csv("stock_data.csv")

# 计算10日简单移动平均
stock_data['SMA10'] = stock_data['Close'].rolling(window=10).mean()

# 生成买入/卖出信号，基于收盘价和10日SMA的关系
stock_data['Signal'] = 0
stock_data['Signal'][10:] = [1 if stock_data['Close'][i] > stock_data['SMA10'][i] else 0 for i in range(10, len(stock_data))]
stock_data['Position'] = stock_data['Signal'].diff()

# 模拟投资组合
initial_capital = 10000
capital = initial_capital
portfolio_data = pd.DataFrame(index=stock_data.index)
portfolio_data['Stock'] = stock_data['Signal'] * capital / stock_data['Close']

# 计算每日市值
portfolio_value = portfolio_data['Stock'].multiply(stock_data['Close'], axis=0)

# 绘制回测后的投资组合价值变化曲线
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Date'], portfolio_value.cumsum() + initial_capital, label='Portfolio Value')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.title('Backtest Portfolio Value Over Time')
plt.legend()
plt.show()
