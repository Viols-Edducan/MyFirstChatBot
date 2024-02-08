import telebot

# Замініть 'YOUR_BOT_TOKEN' на отриманий API ключ від BotFather
bot = telebot.TeleBot('5984708209:AAGEq7givx7l_J9GS5yCRf_3QJoYlrWfJt4')

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Привіт! Я РЕАЛЬНО ТВІЙ чат-бот. Я відповім на команди /start і /help.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)
