import yfinance as yf

tickers = ['MCD', 'SBUX', 'YUM', 'QSR', 'DPZ', 'LKNCY', 'DNUT', 'BRK-A', 'WEN', 'PZZA']

for ticker in tickers:
    data = yf.download(ticker)
    data.to_csv(f'10-largest-fast-food-chains-stock/{ticker}.csv')