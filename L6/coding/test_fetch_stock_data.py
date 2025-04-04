# filename: test_fetch_stock_data.py
import yfinance as yf
from datetime import date, timedelta

# Calculate an adjusted time period for data retrieval
end_date = date.today() - timedelta(days=1)  # Adjustment to avoid weekend non-trading days
start_date = end_date - timedelta(days=30)

# Fetch the stock data
nvidia_stock_data = yf.download('NVDA', start=start_date, end=end_date)

# Display the data
print(nvidia_stock_data)