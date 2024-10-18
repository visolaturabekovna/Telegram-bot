from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Botning ishlash funksiyalari
async def start(update: Update, context):
    await update.message.reply_text("Salom! Men to'tiqush botman. Menga nimadir yozing va men sizga javob beraman!")

async def echo(update: Update, context):
    # Foydalanuvchi kiritgan xabarni qaytaradi
    await update.message.reply_text(update.message.text)

async def stop(update: Update, context):
    await update.message.reply_text("Bot to'xtatildi.")
    context.application.stop()

# Botni ishga tushirish
if __name__ == '__main__':
    # Bot tokenini kiriting (BotFather'dan olgan tokeningiz)
    TOKEN = '7922410202:AAH2YFK7wXhGVBna4H6KaxOjyew1CQUFA6M'

    # ApplicationBuilder orqali botni quramiz
    app = ApplicationBuilder().token(TOKEN).build()

    # Buyruqlarni qo'shamiz
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))

    # Oddiy xabarlarni qaytarish uchun handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni ishga tushiramiz
    print("Bot ishga tushdi...")
    app.run_polling()
