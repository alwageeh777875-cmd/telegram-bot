import os
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

# عند /start
async def start(update, context):
    keyboard = [
        ["📩 مرحباً", "ℹ️ معلومات"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("اختر زر:", reply_markup=reply_markup)


# الرد على الأزرار
async def handle_message(update, context):
    text = update.message.text

    if text == "📩 مرحباً":
        await update.message.reply_text("أهلاً بك 👋")

    elif text == "ℹ️ معلومات":
        await update.message.reply_text("هذا بوت تجريبي 🤖")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("البوت يعمل...")

app.run_polling()
