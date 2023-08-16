import telebot
from datetime import datetime, timedelta
from db import update_or_insert_data, user_exists, get_location_of_user
from api import get_weather , next_day, dict_format
bot = telebot.TeleBot("5980978851:AAH8SF6Zk8pPje2jHmLn0IYdqTUMzYYsFco", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, f"{message.from_user.id}")


@bot.message_handler(commands=['set_location'])
def set_location(message):
        bot.send_message(message.chat.id, "enter location")
        bot.register_next_step_handler(message, get_location)
def get_location(message):

            if user_exists(message.from_user.id) != False:
                update_or_insert_data(message.text,message.from_user.id)
            else:
                update_or_insert_data(data=[message.from_user.id, message.text])

            bot.send_message(message.chat.id, f"location is successfully set")


@bot.message_handler(commands=['today'])
def today_weather(message):

    id = message.from_user.id
    if user_exists(user_id=id) == False:
        bot.send_message(message,"Please set location first")
    else:
        location = get_location_of_user(message.from_user.id)
        data = get_weather(location)

        bot.reply_to(message, f"city : {data.get('location')['city']} \n"
                              f"country : {data.get('location')['country']} \n"
                              f"wind : {data.get('current_observation')['wind']['chill']} / {data.get('current_observation')['wind']['speed']} \n" 
                               f"temperature : {data.get('current_observation')['condition']['temperature']} F \n")


@bot.message_handler(commands=['tomorrow'])
def next_day_weather(message):
    id = message.from_user.id
    if user_exists(user_id=id) == False:
        bot.send_message(message,"Please set location first")
    else:
        location = get_location_of_user(message.from_user.id)
        data = dict_format(get_weather(location).get('forecasts'))
        day = next_day()
        print(data)
        bot.reply_to(message,f" next day : {day} \n"
                             f"low : {data.get(day)['low']} \n"
                             f"high : {data.get(day)['high']} \n"
                             f"weather : {data.get(day)['text']}")


@bot.message_handler(commands=['weekly'])
def next_day_weather(message):
    id = message.from_user.id
    if user_exists(user_id=id) == False:
        bot.send_message(message,"Please set location first")
    else:
        location = get_location_of_user(message.from_user.id)
        data = get_weather(location)['forecasts']
        bot.reply_to(message, f"{data}")

bot.polling()




