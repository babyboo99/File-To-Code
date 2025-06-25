from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN, WEBHOOK_URL
from pack_handler import pack_command, pack_callback_handler, handle_pack_media, auto_finalize
from single_handler import single_command, handle_single_media
from menu import setup_persistent_menu
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Lệnh /Pack và xử lý media tương ứng
app.add_handler(CommandHandler("pack", pack_command))
app.add_handler(CallbackQueryHandler(pack_callback_handler, pattern="^(pack_continue|pack_finish)$"))
app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), handle_pack_media))

# Lệnh /Single
app.add_handler(CommandHandler("single", single_command))
app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), handle_single_media))

# Cài menu cố định
setup_persistent_menu(app.bot)

# Webhook
app.run_webhook(
    listen="0.0.0.0",
    port=8080,
    webhook_url=WEBHOOK_URL
)