import time
import csv
from datetime import datetime
from coingecko import get_price
from alert import check_alert

COINS = ["bitcoin", "ethereum", "solana"]
CSV_FILE = "prices.csv"

def log_price(coin, price, change):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, coin, price, change])

def main():
    print("Starting Crypto Price Tracker...")
    while True:
        for coin in COINS:
            try:
                price, change = get_price(coin)
                print(f"{coin.capitalize()}: ${price:.2f} ({change:.2f}%)")
                check_alert(coin, price, change)
                log_price(coin, price, change)
            except Exception as e:
                print(f"Error fetching data for {coin}: {e}")
        print("-" * 40)
        time.sleep(300)

if __name__ == "__main__":
    main()
