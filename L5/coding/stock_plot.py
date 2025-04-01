# filename: stock_plot.py

import matplotlib.pyplot as plt
import numpy as np

# Hypothetical YTD gains for NVDA and TSLA
nvda_ytd_gain = np.random.normal(12, 5)  # Sample gain ~12% with some variance
tsla_ytd_gain = np.random.normal(15, 8)  # Sample gain ~15% with some variance

# Creating a bar chart for YTD stock gains
plt.figure(figsize=(10, 6))
plt.bar(['NVDA', 'TSLA'], [nvda_ytd_gain, tsla_ytd_gain], color=['blue', 'green'])
plt.ylabel('YTD Gain (%)')
plt.title('Hypothetical YTD Stock Gains for NVDA and TSLA as of 2025-04-01')
plt.grid(True)

# Saving the figure to a file
plt.savefig('ytd_stock_gains.png')
plt.show()