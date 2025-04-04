# filename: fetch_recent_nvidia_stock_data.py
import yfinance as yf
from datetime import date, timedelta

# Calculate the time period for data retrieval
end_date = date.today()
start_date = end_date - timedelta(days=30)

# Fetch the stock data
nvidia_stock_data = yf.download('NVDA', start=start_date, end=end_date)

# Display the data
print(nvidia_stock_data)