from telegram import Update
from telegram.ext import ContextTypes
from storage import load_storage

async def handle_code_to_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("mode") != "code_to_file":
        return

    code = update.message.text.strip().split("_")[-1]
    storage = load_storage()

    if code not in storage:
        await update.message.reply_text("❌ Mã không tồn tại hoặc đã hết hạn.")
        return

    for file_id in storage[code]["files"]:
        await update.message.reply_document(file_id)