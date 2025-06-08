import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# --- Flask App (for Render Health Check) ---
app = Flask(__name__)
@app.route('/')
def index():
    return "I am alive!"

def run_flask_app():
    # The host must be '0.0.0.0' to be accessible by Render
    # The port is dynamically assigned by Render, so we use os.environ.get('PORT')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
# ---------------------------------------------


# --- Telegram Bot Code ---
# Your bot's API token from BotFather
TOKEN = os.environ.get(":")
# Your private channel ID
CHANNEL_ID = os.environ.get("-1002843399419")

# The specific reply for the 'lakshya' keyword
LAKSHYA_REPLY = """
Telegram private group e upload kori lecture recorded form e.
Pw (all sub)
Soms classroom (physics & chemistry)
Soe bangla (pcmb)
Bong mistry (chemistry) pabe

Price 199 rs (payment method upi)
"""

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a message, and my owner will get back to you shortly.')

def handle_lakshya(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(LAKSHYA_REPLY)
    # Forward the user's message to your channel
    if CHANNEL_ID:
        context.bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def handle_message(update: Update, context: CallbackContext) -> None:
    # Forward the user's message to your channel
    if CHANNEL_ID:
        context.bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def run_telegram_bot():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)lakshya'), handle_lakshya))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()
# ---------------------------------------------


# --- Main execution ---
if __name__ == '__main__':
    # Run Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Run Telegram bot in the main thread
    run_telegram_bot()
    
