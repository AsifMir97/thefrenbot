import telegram
from telegram.ext import CommandHandler, Updater

# Replace this with your contract address
CONTRACT_ADDRESS = "0x7a5f1b9acdf5513c8b5fb534ddb3457c85f6274f"
LINK="https://www.dextools.io/app/en/ether/pair-explorer/0x7aae7ae2cf72935bf445f54ada4c4534fdfbb69c"


def ca(update, context):
    message = f"Here is the contract address: {CONTRACT_ADDRESS}\n"
    message += f"Here is the link to the contract on DEXTools: {LINK}"
    update.message.reply_text(message)

def main():
    # Replace this with your API token
    updater = Updater("6088145529:AAEYeB04w21w81b4oGxXQNnYGzi6FragQfo", use_context=True)

    updater.dispatcher.add_handler(CommandHandler("ca", ca))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

