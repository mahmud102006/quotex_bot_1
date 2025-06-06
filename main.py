from telegram.ext import Updater, CommandHandler
import os

# Bot token নিবে environment variable থেকে
TOKEN = os.environ.get("BOTTOKEN")

def start(update, context):
    update.message.reply_text("✅ Bot Active! Type /signal to get a prediction.")

def signal(update, context):
    # এখানে তুমি নিজের prediction logic বসাতে পারো
    update.message.reply_text("📈 Signal: CALL\n⏰ Time: 1 min\n🔮 Confidence: 92%")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signal", signal))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
