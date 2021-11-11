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
        self.date = date

    @classmethod
    def get_data(cls,object):
        data = [int(i) for i in object.date.split('-')]
        if Date.check_data(data[::-1]):
            return data
        else:
            raise ValueError('Неправильная дата')

    @staticmethod
    def check_data(data):
        try:
            datetime(*data)
        except ValueError:
            return False
        return True


if __name__ == '__main__':
    my_class = Date('28-02-2021')
    print(Date.get_data(my_class))