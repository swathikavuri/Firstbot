import os
import telebot

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hello', 'start', 'help'])

def greet(message): 
  firstname = message.from_user.first_name
  lastname = message.from_user.last_name
  print(message.from_user)
  bot.reply_to(message, "Hey " + firstname + " " + lastname + "!!!")

bot.polling()


