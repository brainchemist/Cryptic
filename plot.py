import pandas as pd
import matplotlib.pyplot as plt

def plot_multiple_coins(csv_file="prices.csv", coins=["bitcoin", "ethereum", "solana"]):
    # Read the CSV file
    df = pd.read_csv(csv_file, names=["timestamp", "coin", "price", "change"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["price"] = df["price"].astype(float)

    plt.figure(figsize=(12, 6))

    # Plot each coin
    for coin in coins:
        coin_df = df[df["coin"] == coin]
        plt.plot(coin_df["timestamp"], coin_df["price"], marker='o', label=coin.capitalize())

    plt.title("Crypto Price History")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Call the function
plot_multiple_coins()
