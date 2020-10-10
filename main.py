import telebot
from telebot import types
bot = telebot.TeleBot('1206876123:AAHyHKoSVbxfcHFOf7XzYlGUYwLmoFLUbDA')



@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "Привет, я гороскоп бот")

if __name__ == '__main__':
    bot.polling(none_stop=True)