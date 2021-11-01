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

def type_logger(func):
    def logger(*args,**kwargs):
        print(args)
        print(kwargs)
        for i in args:
            print(f'{func.__name__}({i} : {type(i)})')
            return func(i)
    return logger


@type_logger
def calc_cube(x,y):
   return x ** y

if __name__ == '__main__':
    print(f'Результат: {calc_cube(number=3)}')

