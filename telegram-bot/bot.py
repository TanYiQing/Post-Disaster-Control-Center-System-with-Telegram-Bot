import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
import responses
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PKOB.settings')
django.setup()

API_KEY = "5064342461:AAHp_5cxsL08h8fRgYkB4lprvOVvWOUfYZ4"

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    user = update.message.from_user.first_name
    update.message.reply_text('Hello {}! I\'m ninja-aid_bot. How can I help you today?'.format(user), reply_markup=start_menu_keyboard())


def main_menu(update, context):
    update.callback_query.message.edit_text("Please select a function to continue.",
                                            reply_markup=main_menu_keyboard())


def help_menu(update, context):
    update.callback_query.message.edit_text("What can I help you? Please contact us.",
                                            reply_markup=help_menu_keyboard())


def contact_menu(update, context):
    update.callback_query.message.edit_text("Customer Service Email: ninjaaidpkob@gmail.com",
                                            reply_markup=contact_menu_keyboard())


def about_menu(update, context):
    update.callback_query.message.edit_text("Find out more about us!",
                                            reply_markup=about_menu_keyboard())


def about_me_menu(update, context):
    update.callback_query.message.edit_text("Ninja-aid is a centralized system with the aim of helping the victims "
                                            "facing a disaster to request for help. I'm ninja-aid_bot "
                                            "and I can help you 24 hours to resolve your curiosity. "
                                            "To find out about us, you can visit our website.",
                                            reply_markup=aboutme_menu_keyboard())


def web_menu(update, context):
    update.callback_query.message.edit_text("Our Website:\nhttps://ninja-aid.herokuapp.com/",
                                            reply_markup=website_menu_keyboard())


def get_data_menu(update, context):
    update.callback_query.message.edit_text("Please tell me your Identity Card Number.\nExample: 123456789456",
                                            reply_markup=getinfo_keyboard())


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    response = responses.get_response(text)

    # Bot response
    update.message.reply_text(response)


def handle_data(update, context):
    text = str(update.message.text).lower()
    if text.isnumeric():
        logging.info(f'User ({update.message.chat.id}) says: {text}')
        update.message.reply_text("I'm trying to find information, please wait a moment ...")
        response = responses.get_data(text)
    else:
        response = responses.get_response(text)
    # Bot response
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


def start_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Start Now!', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Get information', callback_data='getdata')],
        [InlineKeyboardButton('Help Center', callback_data='help'),
         InlineKeyboardButton('About This Bot', callback_data='about')]
    ]
    return InlineKeyboardMarkup(keyboard)


def getinfo_keyboard():
    keyboard = [
        [InlineKeyboardButton('Get information', callback_data='getdata')],
        [InlineKeyboardButton('Help Center', callback_data='help'),
         InlineKeyboardButton('About This Bot', callback_data='about')]
    ]
    return InlineKeyboardMarkup(keyboard)


def help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Contact us', callback_data='contactus')],
                [InlineKeyboardButton('Return to the main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def contact_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='help')],
                [InlineKeyboardButton('Return to the main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def about_menu_keyboard():
    keyboard = [[InlineKeyboardButton('About us', callback_data='us'), InlineKeyboardButton('Website', callback_data='web')],
                [InlineKeyboardButton('Return to the main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def aboutme_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='about')],
                [InlineKeyboardButton('Return to the main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def website_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='about')],
                [InlineKeyboardButton('Return to the main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Command
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(help_menu, pattern='help'))
    dp.add_handler(CallbackQueryHandler(contact_menu, pattern='contactus'))
    dp.add_handler(CallbackQueryHandler(about_menu, pattern='about'))
    dp.add_handler(CallbackQueryHandler(about_me_menu, pattern='us'))
    dp.add_handler(CallbackQueryHandler(web_menu, pattern='web'))
    dp.add_handler(CallbackQueryHandler(get_data_menu, pattern='getdata'))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_data))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()