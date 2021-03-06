# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
4.Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""

def val_checker(check):
    def actual_decorator(func):
        def wrapper(*args,**kwargs):
            if check(*args):
                return func(*args)
            else:
               raise ValueError('Wrong val: {0}'.format(*args))
        wrapper.__name__ = func.__name__ # Маскировка декоратора
        return wrapper
    return actual_decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

if __name__=='__main__':
    print(f'Маскировка декоратора: {calc_cube.__name__}')
    print(f'Результат: {calc_cube(4)}')