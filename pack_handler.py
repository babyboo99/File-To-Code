from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
import asyncio, random, string

user_sessions = {}

async def pack_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_sessions[user_id] = {"files": [], "timeout_task": None}
    await update.message.reply_text("Bạn hãy gửi file hoặc media (chuyển tiếp từ nhóm/kênh cũng được).")

    # Sau 5s hiển thị nút
    await asyncio.sleep(5)
    keyboard = [
        [InlineKeyboardButton("➕ Tiếp tục", callback_data="pack_continue")],
        [InlineKeyboardButton("✅ Hoàn thành", callback_data="pack_finish")]
    ]
    await update.message.reply_text("Bạn muốn tiếp tục hay kết thúc?", reply_markup=InlineKeyboardMarkup(keyboard))

async def pack_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "pack_continue":
        await query.edit_message_text("Bot sẽ đợi bạn. Nếu sau 15 phút không có media nào, tôi sẽ tạo mã.")
        task = asyncio.create_task(auto_finalize(user_id, query, context))
        user_sessions[user_id]["timeout_task"] = task

    elif query.data == "pack_finish":
        await query.edit_message_text("Đang tạo mã...")
        await send_code_to_user(user_id, query.message.chat_id, context)

async def handle_pack_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in user_sessions:
        msg = update.message
        if msg.document or msg.photo or msg.video or msg.audio or msg.voice:
            user_sessions[user_id]["files"].append(msg)
        # Reset timer nếu có
        task = user_sessions[user_id].get("timeout_task")
        if task: task.cancel()

async def auto_finalize(user_id, query, context):
    try:
        await asyncio.sleep(900)  # 15 phút
        await context.bot.send_message(query.message.chat_id, "Hết giờ. Đang tạo mã...")
        await send_code_to_user(user_id, query.message.chat_id, context)
    except asyncio.CancelledError:
        pass

async def send_code_to_user(user_id, chat_id, context):
    session = user_sessions.get(user_id, {})
    if not session.get("files"):
        await context.bot.send_message(chat_id, "Không nhận được file nào.")
        return

    # Tạo mã giả định
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    # Gửi chế độ + mã
    keyboard = [
        [InlineKeyboardButton("🌐 Công khai", callback_data="public"),
         InlineKeyboardButton("🔒 Bảo mật", callback_data="private")]
    ]
    await context.bot.send_message(chat_id, f"Mã của bạn là: `{code}`", parse_mode="Markdown",
                                   reply_markup=InlineKeyboardMarkup(keyboard))
    user_sessions.pop(user_id, None)