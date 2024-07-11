import config
import telebot
from random import choice


bot = telebot.TeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message,"""я рибабот привет я повтарюшка рибка""")


@bot.message_handler(commands=['joke'])
def joke_handler(message):
    joke = choice(["Две вещи не стареют — черный юмор и невакцинированные дети", "Акробат умер на батуте, но еще какое-то время продолжал радовать публику.","Однорукий человек заплакал, увидев магазин «секонд-хенд»."])
    bot.reply_to(message, joke)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
