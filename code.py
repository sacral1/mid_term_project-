import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('1178365903:AAGQk6DWymjo6ovoBxcCiAHdos9AKouHIRE')

titles = []
rate = []
description = []
release_date = []
i = 0


def request():
    global titles
    global rate
    global description
    global release_date

    api_key = {"api_key":
               "c714df39f180cce5586ae9609569bb08"}

    r = requests.get('https://api.themoviedb.org/3/trending/movie/day',
                     params=api_key)

    resp = r.text

    dict = json.loads(resp)

    res = dict['results']

    for i in range(len(res)):

        raw = res[i]
        title = raw["title"]
        titles.append(title)
        vote_average = raw['vote_average']
        rate.append(vote_average)
        overview = raw['overview']
        description.append(overview)
        release = raw['release_date']
        release_date.append(release)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Next ->')
    bot.send_message(m.chat.id, "Нажми на кнопку, чтобы получить фильм"
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def suggest(m):
    global i
    request()
    if m.text == 'Next ->':
        if i < 19:
            bot.send_message(m.chat.id, f"Title: {titles[i]}\n"
                             f"Rate: {rate[i]}\n"
                             f"Release date: {release_date[i]}\n"
                             f"Plot twist: {description[i]}")
            i += 1
        else:
            bot.send_message(m.chat.id,
                             "на сегодня все введите команду /start")

    else:
        bot.send_message(m.chat.id, "press on the button")
bot.polling()
