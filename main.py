import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your bot's API token from BotFather
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
# Your private channel ID
CHANNEL_ID = os.environ.get("-1002811758365")

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
    context.bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)


def handle_message(update: Update, context: CallbackContext) -> None:
    # Forward the user's message to your channel
    context.bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'(?i)lakshya'), handle_lakshya))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
