import telebot
import random
from data_service import arr
bot = telebot.TeleBot('1206876123:AAHyHKoSVbxfcHFOf7XzYlGUYwLmoFLUbDA')



@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "Привет, я гороскоп бот")

@bot.message_handler(commands=['try'])
def command_start(message):
    rand = random.randint(0, len(arr)-1)
    bot.send_message(message.chat.id, str(arr[rand]))
if __name__ == '__main__':
    bot.polling(none_stop=True)