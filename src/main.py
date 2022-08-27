import os
import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

API_KEY = os.environ.get('API_KEY')

def start(update: Update, context: CallbackContext):
    """
    `start` is a function that takes two arguments, `update` and `context`, and sends a message to the
    chat that the update originated from
    
    :param update: This is the update object that contains all the information about the incoming
    message
    :type update: Update
    :param context: This is the context of the message. It contains all the information about the
    message
    :type context: CallbackContext
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World!")

def ping(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="pong")

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command, type /help for help")

def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=(update.effective_chat.id, text="bruh fuck off")


if __name__ == '__main__':
    
    print(API_KEY)
    updater = Updater(token=API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    ping_handler = CommandHandler('ping', ping)
    dispatcher.add_handler(ping_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    
    updater.start_polling()

    # idle causes the bot to exit on Ctrl+C. This doesn't happen normally, due to the Updater being executed in a sepparate thread
    updater.idle()