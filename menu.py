from telegram import BotCommand, BotCommandScopeDefault, MenuButtonCommands

def setup_persistent_menu(bot):
    bot.set_my_commands([
        BotCommand("pack", "Gửi nhiều media và lấy mã"),
        BotCommand("single", "Gửi tối đa 10 media và lấy mã"),
    ], scope=BotCommandScopeDefault())
    bot.set_chat_menu_button(menu_button=MenuButtonCommands())