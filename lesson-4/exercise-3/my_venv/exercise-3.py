# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3.* (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в
ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

"""

import re
import requests
from datetime import datetime


def currency_rates(cod_currency):
    # Подготавливаем словарь для возрата данных функцией с ключами (дата,курс)
    result = {'Date':None, 'Value':None}
    # Для того чтобы пользователь передать код курса в любом регистре, мы всегда делаем его UPPER
    cod_currency = cod_currency.upper()
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # C помощью регулярных выражений разбиваем строку
    my_list = re.split('<Valute ID=\"R\S+\">', (req.text).replace('</Valute>', ''))
    # Так как дата находится в первой строке, мы забираем первый элемент списка и ищем по маске с помощью рег. выражений
    re_date = re.search(r"(\d+.){2}\d+",my_list[0]).group()
    # Найденная дата - это строка, преобразовываем ее в вид объекта date
    date = datetime.strptime(re_date, '%d.%m.%Y').date()
    # Помещаем в результирующий словарь
    result['Date'] = date.strftime('%d.%m.%Y')
    for i in my_list[1:]:
        if cod_currency in i:
            match = re.search(r"<NumCode>\d+</NumCode>"
                              r"<CharCode>\S+</CharCode>"
                              r"<Nominal>(\d+)</Nominal>"
                              r"<Name>(.*)</Name>"
                              r"<Value>(.*)</Value>",i).groups()
            result['Value'] = match[2]
            print(f'На {result["Date"]}: {match[0]} {match[1].upper()} cтоит {result["Value"]} руб.')
            break
        else:
            continue
    if not result:
        print(f'На {result["Date"]}: валюты  {cod_currency.upper()} не существует.')
    return result

currency = input('Введите код валюты: ')
func = currency_rates(currency)
print(func)