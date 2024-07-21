import asyncio
from telegram.ext import Application, CommandHandler

# Replace with your actual Telegram bot token
bot_token = ""

async def greet(update, context):
    await update.message.reply_text("Hi!")

def main():
    application = Application.builder().token(bot_token).build()

    # Handler for /hi command
    application.add_handler(CommandHandler("hi", greet))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(stop_signals=None)

if __name__ == "__main__":
    main()