from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '6587257084:AAFgqNYDCK627VFwdqcZy3-haYUTxENI0EQ'

# Command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
            [InlineKeyboardButton("Option 1", callback_data='1')],
            [InlineKeyboardButton("Option 2", callback_data='2')],
            [InlineKeyboardButton("Option 3", callback_data='3')]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose an option:', 
reply_markup=reply_markup)

# Callback query handler to process button presses
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Send a new message based on the selected option
    if query.data == '1':
       query.message.reply_text("You selected Option 1")
    elif query.data == '2':
       query.message.reply_text("You selected Option 2")
    elif query.data == '3':
        query.message.reply_text("You selected Option 3")
    else:
        query.message.reply_text("Invalid option")

def main():
        # Set up the Updater
        updater = Updater(TOKEN, use_context=True)
                                                                                                                
        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher
                                                                                                                            
        # Register command and callback handlers
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CallbackQueryHandler(button))
                                                                                                                                            
        # Start the Bot
        updater.start_polling()
                                                                                                                                                        
        # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
        updater.idle()

if __name__ == '__main__':
         main()
