# 📈 Crypto Price Tracker

This is a Python-based tool that tracks the price of cryptocurrencies (e.g. Bitcoin, Ethereum, Solana) using the CoinGecko API. It logs prices, sends alerts to Discord and via SMS (Twilio), and optionally runs 24/7 inside a Docker container.

---

## 🚀 Features

- Fetches real-time price & % change of selected coins
- Logs prices to `prices.csv`
- Alerts when price changes exceed a threshold
  - ✅ SMS via Twilio
- Optionally runs 24/7 in a Docker container
- Price plotting with `matplotlib`

---

## 📦 Setup (Local Python)

### 1. Clone the repo & set up a virtual environment

```bash
git clone https://github.com/yourusername/crypto-tracker.git
cd crypto-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

python plot.py #After an hour of running the program so you can have enough data to work with
```

##🐳 Docker Usage Guide
1. Build the Docker image

docker build -t crypto-tracker .

2. Run in the background (24/7)

docker run -d \
  --name crypto-tracker \
  --restart always \
  -v $(pwd)/prices.csv:/app/prices.csv \
  --env-file .env \
  crypto-tracker

3. View live logs

docker logs -f crypto-tracker



