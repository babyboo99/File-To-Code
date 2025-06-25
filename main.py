import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)
from config import BOT_TOKEN, WEBHOOK_URL
from commands import start, handle_buttons
from file_to_code import handle_file_to_code
from code_to_file import handle_code_to_file

logging.basicConfig(level=logging.INFO)

# Hàm này sẽ được gọi sau khi app khởi động để thiết lập webhook
async def post_init(application):
    await application.bot.set_webhook(WEBHOOK_URL)

app = (
    ApplicationBuilder()
    .token(BOT_TOKEN)
    .post_init(post_init)  # Gắn webhook tại đây
    .build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))
app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO | filters.VIDEO, handle_file_to_code))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code_to_file))

if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=WEBHOOK_URL
    )