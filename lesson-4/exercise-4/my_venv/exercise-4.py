# -*- coding: utf-8 -*-
# /!usr/bin/env python3

"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

"""

from utils import currency_rates

currency = input('Введите код валюты: ')
my_dict = currency_rates(currency)

print(f'На {my_dict["Date"]}: {my_dict["Nominal"]} {(my_dict["Name"]).upper()} cтоит {my_dict["Value"]} руб.')


