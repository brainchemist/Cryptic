from twilio.rest import Client
import os
from dotenv import load_dotenv

THRESHOLD = 5  # percentage

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_sms_alert(coin, price, change):
    direction = "UP" if change > 0 else "DOWN"
    message = client.messages.create(
        body=f"{coin.capitalize()} is {direction} {abs(change):.2f}%\nPrice: ${price:.2f}",
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )

def check_alert(coin, price, change):
    if abs(change) >= THRESHOLD:
        direction = "up" if change > 0 else "down"
        print(f"🚨 {coin.capitalize()} is {direction} {abs(change):.2f}% to ${price:.2f}")
        send_sms_alert(coin, price, change)
