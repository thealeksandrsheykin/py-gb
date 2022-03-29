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
    def get_data_1(cls,date):
        return [int(i) for i in date.split('-')]

    @classmethod
    def get_data_2(cls,date):
        return cls.check_data([int(i) for i in date.split('-')])

    @staticmethod
    def check_data(data):
        try:
            datetime(*data[::-1])
        except ValueError:
            return f'Ваша дата \"{"-".join([str(i) for i in data])}\" не верна...'
        return Date('-'.join([str(i) for i in data]))

    def __str__(self):
        return f'Дата: {self.date}'


if __name__ == '__main__':
    my_class = Date('20-11-2021')
    my_list_1 = my_class.get_data_1("31-04-2018")  # Дата не верна
    my_list_2 = Date.get_data_1("12-05-2001")      # Дата верна
    print(f'{my_class}  \n'
          f'{"-" * 24}  \n'
          f'{my_list_1} \n'
          f'{my_class.check_data(my_list_1)} \n'
          f'{"-" * 24}  \n'
          f'{my_list_2} \n'
          f'{Date.check_data(my_list_2)} \n'
          f'{"-" * 24}  \n'
          f'{Date.get_data_2("01-00-2020")} \n'     # Дата не верна
          f'{Date.get_data_2("09-09-2020")} \n'     # Дата верна
          f'{"-" * 24}  \n')





