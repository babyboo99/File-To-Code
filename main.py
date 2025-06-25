import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, WEBHOOK_URL
from commands import start
from file_to_code import handle_file_to_code
from code_to_file import handle_code_to_file
from commands import handle_buttons

logging.basicConfig(level=logging.INFO)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))
app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO | filters.VIDEO, handle_file_to_code))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code_to_file))

async def set_webhook():
    await app.bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    import asyncio
    asyncio.run(set_webhook())
    app.run_webhook(listen="0.0.0.0", port=10000, webhook_url=WEBHOOK_URL)