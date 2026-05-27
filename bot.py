import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 أهلاً بك في بوت بطاقات تهاني العيد\n\nاكتب اسمك لإنشاء بطاقة العيد"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
