import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    BOT_TOKEN = "8761763337:AAGisPdNdvU2mFDfgvijoDsvnHTtJVPXips"

bot = telebot.TeleBot(BOT_TOKEN)

# Simple database in memory
users = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = 0
    bot.reply_to(message, f"Welcome to FADI-BOT 😊\n\nYour ID: {user_id}\nBalance: {users[user_id]} coins\n\nCommands:\n/start - Start bot\n/balance - Check balance\n/daily - Daily bonus\n/farm - Farm coins")

@bot.message_handler(commands=['balance'])
def balance(message):
    user_id = message.from_user.id
    bal = users.get(user_id, 0)
    bot.reply_to(message, f"Your balance: {bal} coins")

@bot.message_handler(commands=['daily'])
def daily(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = 0
    users[user_id] += 10
    bot.reply_to(message, f"Daily bonus claimed! +10 coins\nNew Balance: {users[user_id]}")

@bot.message_handler(commands=['farm'])
def farm(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = 0
    users[user_id] += 1
    bot.reply_to(message, f"Farmed 1 coin! ⛏️\nBalance: {users[user_id]}")

print("Bot is running...")
bot.infinity_polling()
