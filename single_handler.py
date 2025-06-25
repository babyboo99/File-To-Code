from telegram import Update
from telegram.ext import ContextTypes
import random, string

user_single = {}

async def single_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_single[user_id] = []
    await update.message.reply_text("Gửi cho tôi tối đa 10 media. Tôi sẽ trả mã tương ứng cho bạn.")

async def handle_single_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_single:
        return

    msg = update.message
    if msg.document or msg.photo or msg.video or msg.audio or msg.voice:
        user_single[user_id].append(msg)

    if len(user_single[user_id]) >= 10:
        # Giới hạn 10 file
        files = user_single[user_id]
        if len(files) > 10:
            files = random.sample(files, 10)

        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        await update.message.reply_text(f"Mã của bạn là: `{code}`", parse_mode="Markdown")
        user_single.pop(user_id)