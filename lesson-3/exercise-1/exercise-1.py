# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
"""

numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}


def num_translate(data):
    return numbers.get(data)


number = input('Введите число на английском от 1-10: ')
print(f'{num_translate(number)}')
