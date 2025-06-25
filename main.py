import asyncio
from telegram.ext import ApplicationBuilder

from commands import start_command, help_command, code_command
from single import single_handler
from pack import pack_handler
from menu import setup_persistent_menu
from config import BOT_TOKEN, WEBHOOK_URL

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Gán lệnh (Command handlers)
    app.add_handler(start_command)
    app.add_handler(help_command)
    app.add_handler(code_command)
    app.add_handler(single_handler)
    app.add_handler(pack_handler)

    # Thiết lập menu cố định
    await setup_persistent_menu(app)

    # Webhook cho Render
    await app.bot.set_webhook(url=WEBHOOK_URL)

    # Chạy bot (dạng webhook)
    await app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    asyncio.run(main())