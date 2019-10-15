import telebot
#from weather import 

bot=telebot.TeleBot('954492072:AAEkgKeEKLHxJnXl9FOnJjwTEVWbkrPFdDE')

#message start bot
mes ="""Команды бота Ushibibot:
     *Погода на сегодня
     *Погода на завтра
     *Смешной анекдот
     *Мемас"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.send_message(message.chat.id, mes)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, "Howdy, how are you doing?")
    if((message.text).lower()=="команды"):
        bot.send_message(message.chat.id, mes)

bot.polling(none_stop=True)