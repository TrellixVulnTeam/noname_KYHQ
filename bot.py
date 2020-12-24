import config
from functions import *
from previous import *
from current import *
import telebot
from telebot import types


idis = [1179243319, 616105665, 444933814, 1095875260, 629229115, 1136054481, 1472282689, 1309473859]
#################################################################
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.id not in idis:
        bot.send_message(message.chat.id, f"Увы вас нету в нашей базе данных!")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Авансы")
        markup.add(item1)

        name = id_to_name(message.from_user.id)


        bot.send_message(message.chat.id, f"Добро пожаловать, {name}!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def avansy(message):
    if message.text == 'Авансы':

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
        item1 = types.KeyboardButton("{}".format(month_rus(b_letter)))
        item2 = types.KeyboardButton("{}".format(month_rus(a_letter)))
        item3 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3)

        msg = bot.send_message(message.chat.id, "За какой месяц?",reply_markup=markup)
        bot.register_next_step_handler(msg, mesyac)

@bot.message_handler(content_types=['text'])
def mesyac(message):

    name = id_to_name(message.from_user.id)

    if message.text == month_rus(b_letter):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)

        msg = bot.send_message(message.chat.id, f'Авансы за {message.text}: \n{prev_trans_all_by_name_date(name)} '
                                                f'\nИтого: {prev_avans_by_name(name)}', reply_markup=markup)
        bot.register_next_step_handler(msg, back)
    elif message.text == month_rus(a_letter):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)

        msg = bot.send_message(message.chat.id, f'Авансы за {message.text}: \n{curr_trans_all_by_name_date(name)} '
                                                f'\nИтого: {curr_avans_by_name(name)}', reply_markup=markup)
        bot.register_next_step_handler(msg, back)
    else:
        welcome(message)
        return

@bot.message_handler(content_types=['text'])
def back(message):
    welcome(message)
    return

bot.polling(none_stop=True)