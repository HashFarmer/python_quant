import pandas as pd
import requests

# Set the API endpoint URL
url = 'https://www.alphavantage.co/query'

# Set the parameters for the API request
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'AAPL',
    'outputsize': 'full',
    'apikey': 'your_api_key'
}

# Make the API request and get the response
response = requests.get(url, params=params)

# Convert the response data into a Pandas DataFrame
data = pd.DataFrame(response.json()['Time Series (Daily)']).T

# Save the data to an Excel file
data.to_excel('AAPL_stock_price_history.xlsx')
