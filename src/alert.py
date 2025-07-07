from twilio.rest import Client
import os
from dotenv import load_dotenv

THRESHOLD = 10  # percentage

load_dotenv()

BOOK_COST = {
    "SPY": 596.53,
    "SOXL": 26.98,
    "FXI": 30.76,
    "NVDA": 235.06,
    "XEQT.TO": 33.94,
    "bitcoin": 151994.16
}

HOLDINGS = {
    "SPY": 8.5634,
    "SOXL": 2.0119,
    "FXI": 5.7026,
    "NVDA": 0.5919,
    "XEQT.TO": 47.7294,
    "bitcoin": 0.016448
}


TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_sms_alert(asset, price, change, profit=None, percent_gain=None):
    direction = "UP" if change > 0 else "DOWN"

    message_body = f"{asset.upper()} is {direction} {abs(change):.2f}%\nPrice: ${price:.2f}"

    if profit is not None:
        message_body += f"\n📈 Total return: +${profit:.2f} (+{percent_gain:.2f}%)"

    message = client.messages.create(
        body=message_body,
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )

def check_alert(asset, price, change):
    book_price = BOOK_COST.get(asset)
    quantity = HOLDINGS.get(asset)

    if book_price is None or quantity is None:
        return

    current_value = price * quantity
    original_value = book_price * quantity
    profit = current_value - original_value
    percent_gain = (profit / original_value) * 100

    if profit > 0:
        print(f"🚀 {asset.upper()} is in profit! +${profit:.2f} (+{percent_gain:.2f}%) → ${price:.2f}")
        send_sms_alert(asset, price, change, profit, percent_gain)
