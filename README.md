# Creation of sample Telegram bot using Python

## Technologies Needed :
  * Telegram account
  * Python IDE (preferred PyCharm)


## Steps involved to create telegram bot 
  1. Genetration of HTTP API token
  2. Accessing HTTP API token in IDE
  3. Writing code to use inbuilt functions in Telegram Bot
  
### 1. Genetration of HTTP API token
  [Telegram Bot Father](https://web.telegram.org/#/im?p=@BotFather)
  ```
  /start
  /newbot
  Set the name of bot
  As seen in below image token is marked in red colour
  ```
![](https://github.com/Regesin/telegrambot/blob/main/telegrambotfather.png)

>Copy the token for later usage

### 2. Accessing HTTP API token in IDE
open IDE and install useful packages to connect with telegram API

```
pip install python-telegram-bot
```

 Create the Updater and pass it your bot's token.
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
 
 


