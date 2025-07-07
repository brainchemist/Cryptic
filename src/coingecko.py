import requests

def get_crypto_price(coin_id="bitcoin"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if coin_id not in data:
        raise ValueError(f"Coin '{coin_id}' not found in API response")

    price = data[coin_id]["usd"]
    change = data[coin_id]["usd_24h_change"]
    return price, change