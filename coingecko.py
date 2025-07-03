import requests

def get_price(coin_id="bitcoin"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    data = response.json()
    price = data[coin_id]['usd']
    change = data[coin_id]['usd_24h_change']
    return price, change
