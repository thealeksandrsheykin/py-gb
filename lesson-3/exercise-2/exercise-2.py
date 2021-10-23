# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One") "Один"
num_translate_adv("two") "два"

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


def num_translate_adv(data):
    if data[0] == data[0].upper():
        return (numbers.get(data.lower())).capitalize()
    else:
        return numbers.get(data)


number = input('Введите число на английском от 1-10: ')
print(f'"{num_translate_adv(number)}"')
