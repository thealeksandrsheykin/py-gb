# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""

from datetime import datetime

class Date:

    def __init__(self,date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @classmethod
    def get_data(cls):

        data = [int(i) for i in cls.date.split('-')]
        print(data)
    #    if Date.check_data(data[::-1]):
    #        return data
    #    else:
    #        raise ValueError('Ваша дата не верна...')

    @staticmethod
    def check_data(data):
        try:
            datetime(*data)
        except ValueError:
            return False
        return True


if __name__ == '__main__':
    my_class = Date('20-11-2021')
    print(f'Первый способ: {my_class.get_data()}')
    #print(f'Второй способ: {Date.get_data("02-05-1990")}')