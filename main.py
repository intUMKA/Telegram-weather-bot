import telebot
import requests
import json


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






