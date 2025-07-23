import telebot
from telebot import types
from auth_data import token
import requests
from datetime import datetime
import random
import string

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    prices = types.KeyboardButton('📊Курсы валют')
    rand = types.KeyboardButton('🎲Рандомайзер')
    ti = types.KeyboardButton('🕰️Время')

    markup.add(prices, rand, ti)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!)'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '📊Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btc = types.KeyboardButton('💵BTC')
            eth = types.KeyboardButton('💵ETH')
            ltc = types.KeyboardButton('💵LTC')
            ton = types.KeyboardButton('💵TON')
            trx = types.KeyboardButton('💵TRX')
            back = types.KeyboardButton('⬅️Назад')

            markup.add(btc, eth, ltc, ton, trx, back)
    
            bot.send_message(message.chat.id, '📊Выберите криптовалюту', reply_markup=markup)

        elif message.text == '💵BTC':
            try:
                req1 = requests.get('https://yobit.net/api/3/ticker/btc_rur')
                req2 = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                res1 = req1.json()
                res2 = req2.json()
                price1 = res1['btc_rur']['sell']
                price2 = res2['btc_usd']['sell']

                bot.send_message(message.chat.id, f"💵BTC\n {datetime.now().strftime('%d-%m-%Y %H:%M')}\nЦена RUB: {price1}\nЦена USD: {price2}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, 'Ошибка!')
        
        elif message.text == '💵ETH':
            try:
                req1 = requests.get('https://yobit.net/api/3/ticker/eth_rur')
                req2 = requests.get('https://yobit.net/api/3/ticker/eth_usd')
                res1 = req1.json()
                res2 = req2.json()
                price1 = res1['eth_rur']['sell']
                price2 = res2['eth_usd']['sell']

                bot.send_message(message.chat.id, f"💵ETH\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\nЦена RUB: {price1}\nЦена USD: {price2}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, 'Ошибка!')

        elif message.text == '💵LTC':
            try:
                req1 = requests.get('https://yobit.net/api/3/ticker/ltc_rur')
                req2 = requests.get('https://yobit.net/api/3/ticker/ltc_usd')
                res1 = req1.json()
                res2 = req2.json()
                price1 = res1['ltc_rur']['sell']
                price2 = res2['ltc_usd']['sell']

                bot.send_message(message.chat.id, f"💵LTC\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\nЦена RUB: {price1}\nЦена USD: {price2}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, 'Ошибка!')

        elif message.text == '💵TON':
            try:
                req1 = requests.get('https://yobit.net/api/3/ticker/ton_rur')
                req2 = requests.get('https://yobit.net/api/3/ticker/ton_usd')
                res1 = req1.json()
                res2 = req2.json()
                price1 = res1['ton_rur']['sell']
                price2 = res2['ton_usd']['sell']

                bot.send_message(message.chat.id, f"💵TON\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\nЦена RUB: {price1}\nЦена USD: {price2}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, 'Ошибка!')

        elif message.text == '💵TRX':
            try:
                req1 = requests.get('https://yobit.net/api/3/ticker/trx_rur')
                req2 = requests.get('https://yobit.net/api/3/ticker/trx_usd')
                res1 = req1.json()
                res2 = req2.json()
                price1 = res1['trx_rur']['sell']
                price2 = res2['trx_usd']['sell']

                bot.send_message(message.chat.id, f"💵TRX\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\nЦена RUB: {price1}\nЦена USD: {price2}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, 'Ошибка!')

        elif message.text == '🎲Рандомайзер':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            integer = types.KeyboardButton('🎲Число в диапазоне (0;100)')
            skull = types.KeyboardButton('🎲Бросить кость')
            password = types.KeyboardButton('🎲Сгенерировать пароль')
            
            back = types.KeyboardButton('⬅️Назад')

            markup.add(integer, skull, password, back)

            bot.send_message(message.chat.id, '🎲Выберите метод', reply_markup=markup)

        elif message.text == '🎲Число в диапазоне (0;100)':
            bot.send_message(message.chat.id, f'Ваше число: {random.randint(0, 100)}')

        elif message.text == '🎲Бросить кость':
            bot.send_message(message.chat.id, f'Ваше число: {random.randint(1, 6)}')

        elif message.text == '🎲Сгенерировать пароль':
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(8))

            bot.send_message(message.chat.id, f'Ваш пароль: {password}')


        elif message.text == '🕰️Время':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            kalt = types.KeyboardButton('🕑\nКалининградское время (KALT)')
            msk = types.KeyboardButton('🕒\nМосковское время (MSK)')
            samt = types.KeyboardButton('🕓\nСамарское время (SAMT)')
            yekt = types.KeyboardButton('🕔\nЕкатеринбургское время (YEKT)')
            omst = types.KeyboardButton('🕕\nОмское время (OMST)')
            krat = types.KeyboardButton('🕖\nКрасноярское время (KRAT)')
            irkt = types.KeyboardButton('🕗\nИркутское время (IRKT)')
            yakt = types.KeyboardButton('🕘\nЯкутское время (YAKT)')
            vlat = types.KeyboardButton('🕙\nВладивостокское время (VLAT)')
            magt = types.KeyboardButton('🕚\nМагаданское время (MAGT)')
            pett = types.KeyboardButton('🕛\nКамчатское время (PETT)')
            back = types.KeyboardButton('⬅️Назад')

             
            markup.add(kalt, msk, samt, yekt, omst, krat, irkt, yakt, vlat, magt, pett, back)

            bot.send_message(message.chat.id, '🕰️Выберите город', reply_markup=markup)

        elif message.text == '🕑\nКалининградское время (KALT)':
            now = datetime.now()
            hours = now.hour - 3
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Калининграде - {hours}:{minutes}')

        elif message.text == '🕒\nМосковское время (MSK)':
            now = datetime.now()
            hours = now.hour - 2
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Москве - {hours}:{minutes}')

        elif message.text == '🕓\nСамарское время (SAMT)':
            now = datetime.now()
            hours = now.hour - 1
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Самаре - {hours}:{minutes}')

        elif message.text == '🕔\nЕкатеринбургское время (YEKT)':
            now = datetime.now()
            hours = now.hour
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Екатеринбурге - {hours}:{minutes}')

        elif message.text == '🕕\nОмское время (OMST)':
            now = datetime.now()
            hours = now.hour + 1
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Омске - {hours}:{minutes}')

        elif message.text == '🕖\nКрасноярское время (KRAT)':
            now = datetime.now()
            hours = now.hour +2
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Красноярске - {hours}:{minutes}')

        elif message.text == '🕗\nИркутское время (IRKT)':
            now = datetime.now()
            hours = now.hour + 3
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Иркутске - {hours}:{minutes}')

        elif message.text == '🕘\nЯкутское время (YAKT)':
            now = datetime.now()
            hours = now.hour + 4
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Якутии - {hours}:{minutes}')

        elif message.text == '🕙\nВладивостокское время (VLAT)':
            now = datetime.now()
            hours = now.hour + 5
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время во Владивостоке - {hours}:{minutes}')

        elif message.text == '🕚\nМагаданское время (MAGT)':
            now = datetime.now()
            hours = now.hour + 6
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время в Магадане - {hours}:{minutes}')

        elif message.text == '🕛\nКамчатское время (PETT)':
            now = datetime.now()
            hours = now.hour + 7
            if hours < 0:
                hours += 24
            if hours >= 24:
                hours -= 24
            minutes = now.minute

            bot.send_message(message.chat.id, f'Время на Камчатке - {hours}:{minutes}')

        

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            prices = types.KeyboardButton('📊Курсы валют')
            rand = types.KeyboardButton('🎲Рандомайзер')
            ti = types.KeyboardButton('🕰️Время')

            markup.add(prices, rand, ti)

            bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)

bot.polling(non_stop=True)