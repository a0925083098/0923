from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]  # 從環境變數取得 Token

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("收到你的訊息啦～ 👋")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, handle_message))

print("機器人已啟動 🚀")
app.run_polling()
