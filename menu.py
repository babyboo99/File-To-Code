from telegram import BotCommand, BotCommandScopeDefault
from telegram.ext import Application

async def setup_persistent_menu(app: Application):
    commands = [
        BotCommand("start", "Khởi động bot"),
        BotCommand("help", "Hướng dẫn sử dụng"),
        BotCommand("pack", "📤 Gửi nhiều media (Pack Mode)"),
        BotCommand("single", "📤 Gửi tối đa 10 media (Single Mode)"),
        BotCommand("code", "📥 Nhập code để lấy lại file"),
    ]

    await app.bot.set_my_commands(commands, scope=BotCommandScopeDefault())