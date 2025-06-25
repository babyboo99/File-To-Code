from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Hàm khởi động khi người dùng gửi /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📤 File to Code", callback_data="file_to_code")],
        [InlineKeyboardButton("📥 Code to File", callback_data="code_to_file")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Chọn một chức năng:", reply_markup=reply_markup)

# Hàm xử lý khi người dùng bấm vào các nút
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "file_to_code":
        context.user_data["mode"] = "file_to_code"
        keyboard = [[InlineKeyboardButton("❌ Kết thúc", callback_data="end")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧾 Gửi file/media để nhận mã. Bạn có 30 phút.\nNhấn ❌ Kết thúc khi xong.",
            reply_markup=reply_markup
        )

    elif query.data == "code_to_file":
        context.user_data["mode"] = "code_to_file"
        keyboard = [[InlineKeyboardButton("❌ Kết thúc", callback_data="end")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💾 Gửi đoạn mã để tạo lại file.\nNhấn ❌ Kết thúc khi xong.",
            reply_markup=reply_markup
        )

    elif query.data == "end":
    context.user_data.clear()
    await query.message.reply_text("✅ Phiên làm việc đã kết thúc. Gửi /start để bắt đầu lại.")