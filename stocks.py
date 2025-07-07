import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    if len(hist) < 2:
        raise ValueError(f"Not enough data for {ticker}")

    latest = hist.iloc[-1]["Close"]
    previous = hist.iloc[-2]["Close"]
    change_percent = ((latest - previous) / previous) * 100

    return latest, change_percent
