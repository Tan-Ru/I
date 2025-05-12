from flask import Flask, render_template
from twilio.rest import Client
import os

app = Flask(__name__)

# Load from environment variables (Render will use these)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/")
def index():
    try:
        message = client.messages.create(
            body="Smoke detected in mall!",
            from_=TWILIO_FROM_NUMBER,
            to=TO_NUMBER
        )
        return render_template("index.html", status="💬Successfully sent message!")
    except Exception as e:
        return render_template("index.html", status="Error sending SMS")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
