from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8682736647:AAEplBFLa9BcYjt4ijNuJtzekPNp6C2iUqQ"

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت يعمل بنجاح ✅")

# إنشاء التطبيق
app = Application.builder().token(TOKEN).build()

# إضافة الأمر
app.add_handler(CommandHandler("start", start))

# تشغيل البوت
print("Bot is running...")
app.run_polling()
