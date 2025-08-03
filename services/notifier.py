import requests
import config

def send_alert(message):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print("❌ Telegram alert failed:", response.text)
    except Exception as e:
        print("❌ Error sending Telegram alert:", e)