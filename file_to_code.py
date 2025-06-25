import os, json, random, string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from storage import load_storage, save_storage

def generate_code(length=12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

async def handle_file_to_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("mode") != "file_to_code":
        return

    user_id = str(update.effective_user.id)
    storage = load_storage()

    if user_id not in storage:
        storage[user_id] = {"files": []}

    file_id = None
    if update.message.document:
        file_id = update.message.document.file_id
    elif update.message.photo:
        file_id = update.message.photo[-1].file_id
    elif update.message.video:
        file_id = update.message.video.file_id

    if file_id:
        storage[user_id]["files"].append(file_id)
        save_storage(storage)

        keyboard = [
            [InlineKeyboardButton("✅ Kết thúc", callback_data="done")],
        ]
        await update.message.reply_text(
            f"📦 Đã nhận file. Gửi tiếp nếu muốn. Khi xong, bấm Kết thúc.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    if update.callback_query and update.callback_query.data == "done":
        code = generate_code()
        storage[code] = storage.pop(user_id)
        save_storage(storage)
        await update.message.reply_text(f"🎉 Mã của bạn là: media_code_{len(storage[code]['files'])}_{code}")