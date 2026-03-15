import telebot
from telebot import types

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_start_message(message):
    # Create an inline button
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Open SuperFishingPro', url='https://SrvlordVAS.github.io/SuperFishingPro/')
    markup.add(button)
    
    # Send the message with the inline button
    bot.send_message(message.chat.id, 'Welcome to the Super Fishing Pro bot! Click the button below to open the mini app:', reply_markup=markup)

# Start the bot
bot.polling()