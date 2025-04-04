# filename: fetch_nvidia_stock_data.py
import yfinance as yf

# Set the time period for data retrieval
start_date = '2025-03-05'
end_date = '2025-04-05'

# Fetch the stock data
nvidia_stock_data = yf.download('NVDA', start=start_date, end=end_date)

# Display the data
print(nvidia_stock_data)