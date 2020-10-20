import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
from telegram.files import video

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

STATEMENT, USER, NUMBER, PHOTO, VIDEO, LOCATION = range(6)


def start(update, context):
    reply_keyboard = [['Natural Disasters', 'Man-Made Disasters', 'Complex Emergencies', 'Pandemic Emergencies']]
    update.message.reply_text(
        'Hi! My name is Epidemic Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Please Select any one disaster ',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return STATEMENT


def disaster(update, context):
    user = update.message.from_user
    logger.info("STATEMENT of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thanks for selecting one disaster, Can you share your Name.')

    return USER


def name(update, context):
    user = update.message.from_user
    name_obj = update.message.text
    print("Name of the user is " + name_obj)
    update.message.reply_text('Thanks for the Name, Please Send us your number')

    return NUMBER


def number(update, context):
    user = update.message.from_user
    number_obj = update.message.text
    print("Number of the User is : " + number_obj)
    update.message.reply_text('Thanks for the Number, Please Send me the photo')

    return PHOTO


def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download()
    logger.info("Photo of %s", user.first_name)
    update.message.reply_text('Please send us the small video ! ')

    return VIDEO


def video(update, context):
    user = update.message.from_user
    video_file = update.message.video.get_file()
    video_file.download()
    logger.info("Video is downloaded")
    update.message.reply_text('Please send us the Location!')

    return LOCATION


def location(update, context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    temp = str(user_location.latitude) + " " + str(user_location.longitude)
    print("The Location is " + temp)
    update.message.reply_text('Location has been Updated in our Database! '
                              'We will Send a response teams as soon as possible.')

    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1249654031:AAE1d-YNaVtNCCjXKkRSKKt1-ikdF1KOZCk", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conf_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={

            STATEMENT: [MessageHandler(
                Filters.regex('^(Natural Disasters|Man-Made Disasters|Complex Emergencies|Pandemic Emergencies)$'),
                disaster)],

            USER: [MessageHandler(Filters.text, name)],

            NUMBER: [MessageHandler(Filters.text, number)],

            PHOTO: [MessageHandler(Filters.photo, photo)],

            VIDEO: [MessageHandler(Filters.video, video)],

            LOCATION: [MessageHandler(Filters.location, location)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conf_handler)

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()