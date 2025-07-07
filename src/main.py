from coingecko import get_crypto_price
from stocks import get_stock_price
from alert import check_alert
import time
import csv
from datetime import datetime



CRYPTO_COINS = ["bitcoin", "ethereum", "solana"]
STOCKS = ["FXI", "NVDA", "SOXL", "SPY", "XEQT.TO"]
CSV_FILE = "../prices.csv"

def log_price(name, price, change):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, name, price, change])

print("Fetching crypto prices...")

def main():
    print("Starting Crypto & Stock Tracker...")
    while True:
        for coin in CRYPTO_COINS:
            try:
                price, change = get_crypto_price(coin)
                print(f"{coin.capitalize()}: ${price:.2f} ({change:.2f}%)")
                check_alert(coin, price, change)
                log_price(coin, price, change)
            except Exception as e:
                print(f"Error fetching data for {coin}: {e}")

        for ticker in STOCKS:
            try:
                price, change = get_stock_price(ticker)
                print(f"{ticker}: ${price:.2f} ({change:.2f}%)")
                check_alert(ticker, price, change)
                log_price(ticker, price, change)
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")

        print("-" * 40)
        time.sleep(300)

if __name__ == "__main__":
    main()