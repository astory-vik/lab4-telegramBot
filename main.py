import telebot
from telebot import types
import random
from data_service import RandomHoroscope
from telebot import types
bot = telebot.TeleBot('1206876123:AAHyHKoSVbxfcHFOf7XzYlGUYwLmoFLUbDA')
markup = types.ReplyKeyboardMarkup()
markup.row('Выдать гороскоп', 'help')




@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "Привет, я гороскоп бот")


@bot.message_handler(content_types=['text'])
def send_horoscope(message):
    if message.text == 'Выдать гороскоп':
        bot.send_message(message.chat.id, RandomHoroscope())
    elif message.text.lower() == 'help':
        bot.send_message(message.chat.id, "Привет я гороскоп БОТ, я предсказываю будущее и не только)")


# @bot.message_handler(commands=['try'])
# def command_start(message):
#   rand = random.randint(0, len(arr)-1)
#   bot.send_message(message.chat.id, str(arr[rand]))

if __name__ == '__main__':
    markup = types.ReplyKeyboardMarkup()
    markup.row('Выдать гороскоп', 'help')
    bot.polling(none_stop=True)

