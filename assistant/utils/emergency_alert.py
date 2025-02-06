from twilio.rest import Client

TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
EMERGENCY_CONTACT = "recipient_phone_number"

def send_emergency_alert():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Emergency! Please check in immediately.",
        from_=TWILIO_PHONE_NUMBER,
        to=EMERGENCY_CONTACT
    )
    return f"Emergency alert sent! SID: {message.sid}"
