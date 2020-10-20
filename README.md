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


    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("Place your Token  Here", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conf_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            States that you want to perform
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
 
 


