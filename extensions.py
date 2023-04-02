import requests
import json
from config import keys


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(player_input):
        player_input = player_input.split(' ')
        if len(player_input) > 3:
            print(len(player_input))
            raise ConversionException('Параметров > 3')
        if len(player_input) < 3:
            print(len(player_input))
            raise ConversionException('Параметров < 3')
        from_, to_, amount = player_input
        try:
            fsym = keys[from_]
        except KeyError:
            raise ConversionException(f'{from_} отсутствует в обработке')
        try:
            tsyms = keys[to_]
        except KeyError:
            raise ConversionException(f'{to_} отсутствует в обработке')
        if from_ == to_:
            raise ConversionException(f'Ввели одну и ту же валюту: {from_} к {to_} : 1 к 1')
        try:
            amount_f = float(amount)
        except ValueError:
            raise ConversionException(f'Не обработалось количество: {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsyms}')
        msg = f'{amount} {from_} это {round(amount_f * json.loads(r.content)[tsyms], 2)} {to_}'
        return msg
