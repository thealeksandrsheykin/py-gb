# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
2.Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
"http://www.cbr.ru/scripts/XML_daily.asp".
Рекомендация: выполнить предварительно запрос к API в обычном браузере,посмотреть содержимое ответа. Можно ли, используя
только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
Подумайте:
Есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не
зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""

import requests
import xml.etree.ElementTree as ET

# Функция, которая вытаскивает данные из xml файла без специализированной библиотеки
def currency_rates(cod_currency):
    result = None
    cod_currency = cod_currency.upper()
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # Разбиваем строку по слову "Valute"
    my_list = (req.text).split('<Valute')
    for i in my_list:
        # Находим строку в которой содержится наш запрос
        if cod_currency in i:
            # Находим индексы и преобразовываем строку
            data = i[i.find('<Name>'):]
            data = data[:data.find('</Value>')]
            data = data.replace('<Name>', '')
            # Разбиваем строку на две переменные (названия валюты,курс)
            name,result = data.split('</Name><Value>')
            break
        else:
            name = cod_currency
            continue
    if result:
        print(f'На данный момент один {name.upper()} cтоит {result} руб.')
    else:
        print(f'На данный момент валюты  {name.upper()} не существует.')
    # Возвращаем курс
    return result


# Функция, которая парсит xml файл с помощью специализированной библиотеки
def currency_rates_adv(cod_currency):
    result = None
    my_dict = dict()
    cod_currency = cod_currency.upper()
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(req.text)
    for i in tree.iter('Valute'):
        my_dict[i[1].text] = {'Name':i[3].text,'Value':i[4].text}
    if my_dict.get(cod_currency, None):
        result = my_dict[cod_currency]["Value"]
        print(f'На данный момент один {(my_dict[cod_currency]["Name"]).upper()} cтоит {result} руб.')
    else:
        print(f'На данный момент валюты  {cod_currency.upper()} не существует.')
    return result


currency = input('Введите код валюты: ')
func_1 = currency_rates(currency)
print(func_1)
print(f'------------')
func_2 = currency_rates_adv(currency)
print(func_2)
