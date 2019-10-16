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
    bot.set_chat_photo(message.chat.id,"logo.jpg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mess=(message.text).lower()
    if(mess=="команды"):
        bot.send_message(message.chat.id, mes)
    elif(mess=="погода на сегодня"):
        bot.send_message(message.chat.id, mes)
    elif(mess=="погода на завтра"):
        bot.send_message(message.chat.id, mes)
    elif(mess=="смешной анекдот"):
        bot.send_message(message.chat.id, mes)
    elif(mess=="мемас"):
        bot.send_message(message.chat.id, mes)
    else:
        bot.reply_to(message, "Простите, но еще нет такой команды!")

bot.polling(none_stop=True)