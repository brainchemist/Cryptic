
#  Cryptic - Crypto & Stock Tracker with SMS Alerts

Cryptic is a Python-based tracker that monitors the prices of selected cryptocurrencies and stocks. If the price changes exceed a defined threshold or your investments turn profitable, it sends SMS alerts via Twilio.

##  Features

-  Tracks real-time prices of crypto (via CoinGecko) and stocks (via Yahoo Finance)
-  Sends SMS alerts if thresholds are exceeded or if you're in profit
-  Logs all price data into a `prices.csv` file
-  Fully containerized with Docker support
-  Auto-restarts using `--restart always` in Docker
-  Uses `.env` file to securely store sensitive data

##  Technologies Used

- Python 3.10
- Docker
- Twilio API
- CoinGecko API
- yFinance (Yahoo Finance)
- Pandas, CSV
- dotenv

##  Project Structure

```
Cryptic/
├── Dockerfile
├── docker.sh
├── prices.csv
├── requirements.txt
├── readme.md
├── src/
│   ├── main.py
│   ├── alert.py
│   ├── coingecko.py
│   └── stocks.py
└── .env
```

##  Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Cryptic.git
cd Cryptic
```

### 2. Create `.env` File

```env
# .env
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM=your_twilio_phone_number
TWILIO_TO=your_verified_phone_number
```

### 3. Build and Run with Docker

```bash
chmod +x docker.sh
./docker.sh
```

This script will:
- Stop and remove any existing `cryptic` container
- Rebuild the image
- Start a new container with:
  - Logs mounted to `prices.csv`
  - Twilio credentials loaded from `.env`

##  Assets Tracked

### Crypto (via CoinGecko)
- Bitcoin
- Ethereum
- Solana

### Stocks/ETFs (via Yahoo Finance)
- FXI
- NVDA
- SOXL
- SPY
- XEQT (`XEQT.TO` in code)

##  SMS Alerts

You'll receive a message like this:
```
🚨 NVDA is UP 5.42%
Price: $135.21
Profit: +$13.21 CAD (+10.2%)
```

### Profit alerts use:
- Your average book cost per asset
- Your quantity per asset
- Threshold defined in `alert.py` (default: 10%) I used 10% because I am looking for a longterm return

##  Development (without Docker)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

##  Notes

- Set `THRESHOLD` in `alert.py` to control SMS sensitivity
- `prices.csv` is automatically created and appended every 5 minutes
- Docker ensures your tracker keeps running with `--restart always`

## TODO

- [ ] Web dashboard via Streamlit
- [ ] Email alert option #I don't think I will do this one
- [ ] Multi-currency support 

##  Author

**Zack (BrainChemist)**  
[GitHub](https://github.com/brainchemist)

## License

MIT License
