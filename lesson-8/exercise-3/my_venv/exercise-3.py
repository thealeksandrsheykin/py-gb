# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
3.Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>

Примечание:
если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?

Сможете ли вывести имя функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)

"""

from functools import wraps

def type_logger(func):
    print(f'Оборачиваемая функция: {func}\n'
          f'Тип: {type(func)}\n')
    @wraps(func)
    def wrapper(*args,**kwargs):
        if kwargs:
            data = [j for i,j in kwargs.items()]
        else:
            data = list(args)
        for i in data:
            print(f'{func.__name__} ({i}: {type(i)}) Результат работы функции: {func(i)}')
    return wrapper



@type_logger
def calc_cube(x):
   return  x**3

if __name__ == '__main__':
    print(f'Маскировка декоратора: {calc_cube.__name__}\n')
    calc_cube(2)
    print()
    calc_cube(3,4,5,6)
    print()
    calc_cube(number_1=7)
    print()
    calc_cube(number_1=8,number_2=9,number_3=10,number_4=11)


