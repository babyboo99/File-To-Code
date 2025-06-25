from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📤 File to Code", callback_data="file_to_code")],
        [InlineKeyboardButton("📥 Code to File", callback_data="code_to_file")]
    ]
    await update.message.reply_text("Chọn một chức năng:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "file_to_code":
        context.user_data["mode"] = "file_to_code"
        await query.edit_message_text("Gửi file/media để nhận mã. Bạn có 30 phút. Nhấn 'Kết thúc' khi xong.")
    elif query.data == "code_to_file":
        context.user_data["mode"] = "code_to_file"
        await query.edit_message_text("Vui lòng gửi mã để lấy lại file.")