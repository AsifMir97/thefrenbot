import telegram
import time
from telegram.ext import CommandHandler, Updater

# Replace this with your contract address
CONTRACT_ADDRESS = "0x7a5f1b9acdf5513c8b5fb534ddb3457c85f6274f"
LINK="https://www.dextools.io/app/en/ether/pair-explorer/0x7aae7ae2cf72935bf445f54ada4c4534fdfbb69c"


def ca(update, context):
    message = f"Here is the contract address: {CONTRACT_ADDRESS}\n"
    message += f"Here is the link to the contract on DEXTools: {LINK}"
    update.message.reply_text(message)


def website(update, context):
    message = f"Here is the website  : https://fren.finance/"
    update.message.reply_text(message)

def engage_users(update, context):
    caption = "Hey everyone, just wanted to remind you to keep Shilling $FREN! 🚀💎🙌"
    with open("/frencool.jpg", "rb") as image:
        context.bot.send_photo(photo=image, caption=caption)


def main():
    # Replace this with your API token
    updater = Updater("6088145529:AAEYeB04w21w81b4oGxXQNnYGzi6FragQfo", use_context=True)

#command handlers 
    updater.dispatcher.add_handler(CommandHandler("ca", ca))
    updater.dispatcher.add_handler(CommandHandler("website", website))

    updater.start_polling()
# Schedule the engagement function to run every 15 minutes
    job_queue = updater.job_queue
    job_queue.run_repeating(engage_users, interval=900, first=0)
# Keep the bot running until stopped manually
    updater.idle()

if __name__ == '__main__':
    main()

