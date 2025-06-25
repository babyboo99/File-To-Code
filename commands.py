from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xin chào! Tôi là bot hỗ trợ mã hóa và giải mã file/media.\n\n"
        "📦 /pack - Gửi hoặc chuyển tiếp nhiều media từ nhóm/kênh công khai.\n"
        "📤 /single - Gửi tối đa 10 media để tạo mã tương ứng.\n"
        "📥 /code - Giải mã để tải về media.\n"
        "ℹ️ Gõ /help để biết thêm chi tiết."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Hướng dẫn sử dụng bot:\n\n"
        "📦 /pack: Cho phép bạn gửi hoặc chuyển tiếp nhiều media.\n"
        "   - Sau 5 giây, bot hỏi bạn muốn tiếp tục hay kết thúc.\n"
        "   - Nếu không gửi thêm sau 15 phút, bot sẽ tự tổng hợp.\n\n"
        "📤 /single: Gửi tối đa 10 media (trực tiếp hoặc chuyển tiếp).\n"
        "   - Nếu vượt quá, bot sẽ tự xoá ngẫu nhiên để còn 10 file.\n\n"
        "📥 /code <mã>: Dán mã đã nhận để tải lại media.\n"
        "   - Nếu mã bảo mật, bạn sẽ được yêu cầu nhập mật khẩu.\n\n"
        "🔒 Mã có thể ở chế độ công khai hoặc riêng tư tùy bạn lựa chọn."
    )

async def code_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📥 Hãy gửi mã code bạn đã nhận để tôi kiểm tra và gửi lại file tương ứng.\n"
        "Ví dụ: `/code p_abcxyz123`"
    )
