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
import re
import requests
import xml.etree.ElementTree as ET

# Функция, которая вытаскивает данные из xml файла без специализированной библиотеки
def currency_rates(cod_currency):
    result = None
    cod_currency = cod_currency.upper()
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # С помощью регулярных выражений разбиваем строку и находим нужные нам значения помещая их в кортеж
    my_list = re.split("<Valute ID=\"R\S+\">", (req.text).replace('</Valute>', ''))
    for i in my_list:
        if cod_currency in i:
            match = re.search(r'<NumCode>\d+</NumCode>'
                              r'<CharCode>(\S+)</CharCode>'
                              r'<Nominal>(\d+)</Nominal>'
                              r'<Name>(\S+\s+\S+)</Name>'
                              r'<Value>(\S+)</Value>',i).groups()
            result = match[3]
            print(f'На данный момент {match[1]} {match[2].upper()} cтоит {result} руб.')
            break
        else:
            continue
    if not result:
        print(f'На данный момент валюты  {cod_currency.upper()} не существует.')
    return result



# Функция, которая парсит xml файл с помощью специализированной библиотеки
def currency_rates_adv(cod_currency):
    result = None
    my_dict = dict()
    cod_currency = cod_currency.upper()
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(req.text)
    for i in tree.iter('Valute'):
        my_dict[i[1].text] = {'Nominal':i[2].text,'Name':i[3].text,'Value':i[4].text}
    if my_dict.get(cod_currency, None):
        nominal = my_dict[cod_currency]["Nominal"]
        name = (my_dict[cod_currency]["Name"]).upper()
        result = my_dict[cod_currency]["Value"]
        print(f'На данный момент {nominal} {name} cтоит {result} руб.')
    else:
        print(f'На данный момент валюты  {cod_currency.upper()} не существует.')
    return result


currency = input('Введите код валюты: ')
func_1 = currency_rates(currency)
print(func_1)
print(f'------------')
func_2 = currency_rates_adv(currency)
print(func_2)
