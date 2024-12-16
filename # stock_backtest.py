import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子以便结果可重复
np.random.seed(42)

# 假设的股票历史数据（具有一定的波动性）
days = 60  # 假设60天的数据
initial_price = 100  # 初始股价
price_changes = np.random.randn(days) * 2  # 随机生成波动，每天波动为2元左右

# 创建股价序列，基于初始股价和随机波动
prices = initial_price + np.cumsum(price_changes)  # 累积加总波动生成股价

# 构造日期序列
dates = pd.date_range(start='2023-01-01', periods=days, freq='D')

# 创建DataFrame
stock_data = pd.DataFrame({
    'Date': dates,
    'Close': prices
})

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
plt.plot(stock_data['Date'], portfolio_value.cumsum() + initial_capital, label='Portfolio Value', color='b')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.title('Backtest Portfolio Value Over Time')
plt.legend()
plt.xticks(rotation=45)  # 使日期标签不重叠
plt.show()
