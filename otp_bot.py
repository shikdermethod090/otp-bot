import os
import time
import re
from flask import Flask
import telegram
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL")
DATA_URL = os.getenv("DATA_URL")

bot = telegram.Bot(token=BOT_TOKEN)

def send_to_telegram(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode=telegram.constants.ParseMode.HTML)

def run_bot():
    while True:
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)

            driver.get(LOGIN_URL)
            # Login logic here (simplified for demo)
            # ...
            # Scrape OTP and send
            send_to_telegram("✅ Bot is alive and scraping!")

            driver.quit()
        except Exception as e:
            send_to_telegram(f"❌ Error: {e}")
        time.sleep(60)

# Start dummy Flask app to keep Render service alive
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
