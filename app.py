import telebot
from config import TOKEN, keys
from extensions import CryptoConverter, ConversionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def test_echo(message: telebot.types.Message):
    text = 'Введите: <имя валюты>' \
           ' <имя валюты в какую перевести>' \
           ' <количество>\nДля вывода доступных валют введите: </values>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def val(message: telebot.types.Message):
    text = 'Доступно: \n'
    for key in keys:
        text += (key + '\n')
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        msg = CryptoConverter.get_price(message.text)
    except ConversionException as e:
        msg = f'Ошибка пользователя.\n{e}'
    except Exception as e:
        print(e)
        msg = f'Ошибка бота.\n{e}'
    finally:
        bot.reply_to(message, msg)


bot.polling()
