# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import re
import requests
from datetime import datetime


def currency_rates(cod_currency):
    key = ('Nominal','Name','Value')
    result = None
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    my_list = re.split('<Valute ID=\"R\S+\">', (req.text).replace('</Valute>', ''))

    for i in my_list[1:]:
        if cod_currency.upper() in i:
            re_date = re.search(r"(\d+.){2}\d+", my_list[0]).group()
            date = datetime.strptime(re_date, '%d.%m.%Y').date()
            value = re.search(r"<NumCode>\d+</NumCode>"
                              r"<CharCode>\S+</CharCode>"
                              r"<Nominal>(\d+)</Nominal>"
                              r"<Name>(.*)</Name>"
                              r"<Value>(.*)</Value>",i).groups()
            result = {key[j]: value[j] for j,_ in enumerate(value)}
            result['Date'] = date.strftime('%d.%m.%Y')
            break
        else:
            continue

    return result

if __name__ == '__main__':
    cod_currency = input('Введите код: ')
    my_dict = currency_rates(cod_currency)
    print(my_dict)