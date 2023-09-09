import telebot
import requests
import json
#import sqlite3
#from telebot import types

bot = telebot.TeleBot('6637484481:AAFWFD0qftAqF9DklO7-8AfPjgi1KxgoUMk')
API = '6433f82a0235dcb9df58055f36b63479'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi, please enter your city name:')


@bot.message_handler(content_types= ['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Weather now is: {data["main"]["temp"]}')

        image = 'sunny.jpg' if temp > 5.0 else 'clouds and suuny.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'That`s a dog shit, try to enter a real city name')

bot.polling(none_stop=True)













#name = None




"""cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()  


   bot.send_message(message.chat.id, 'Hi, let`s registrate you! Please enter your name:')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, ' Please enter your password:')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('telebot.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s') " % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('List of users', callback_data='users'))
    bot.send_message(message.chat.id, 'You`ve been registrated!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('telebot.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, password: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)
"""





#@bot.message_handler(commands=['start'])
#def main(message):
#bot.send_message(message.chat.id, 'Meow!')


#photo = open('C:\Users\Ivan Todorashko\Pictures\Saved Pictures\umka.jpg', 'rb')


#@bot.message_handler(commands=['pic'])
#def main(message):
#    bot.send_photo(message.chat.id, photo)