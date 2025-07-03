import pandas as pd
import matplotlib.pyplot as plt

def plot_price_history(csv_file="prices.csv", coin="bitcoin"):
    df = pd.read_csv(csv_file, names=["timestamp", "coin", "price", "change"])
    df = df[df["coin"] == coin]
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["price"] = df["price"].astype(float)

    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["price"], marker='o')
    plt.title(f"{coin.capitalize()} Price Over Time")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_price_history("prices.csv", "bitcoin")

