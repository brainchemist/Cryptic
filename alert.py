from twilio.rest import Client

THRESHOLD = 5  # percentage

TWILIO_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_FROM = "+12314403719"
TWILIO_TO = "+14388331822"

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
