import pandas as pd
import matplotlib.pyplot as plt

def plot_each_coin_in_same_window(csv_file="prices.csv", coins=["bitcoin", "ethereum", "solana"]):
    df = pd.read_csv(csv_file, names=["timestamp", "coin", "price", "change"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["price"] = df["price"].astype(float)

    num_coins = len(coins)
    fig, axs = plt.subplots(num_coins, 1, figsize=(12, 4 * num_coins), sharex=True)

    for i, coin in enumerate(coins):
        coin_df = df[df["coin"] == coin]

        if coin_df.empty:
            axs[i].text(0.5, 0.5, f"No data for {coin}", ha='center')
            continue

        axs[i].plot(coin_df["timestamp"], coin_df["price"], marker='o')
        axs[i].set_title(f"{coin.capitalize()} Price Over Time")
        axs[i].set_ylabel("Price (USD)")
        axs[i].grid(True)

    plt.xlabel("Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_each_coin_in_same_window()
