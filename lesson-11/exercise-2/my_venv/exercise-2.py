# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
2.Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""

class My_Exception(Exception):
    def __init__(self,text=None):
        self.text = text

    def __str__(self):
        if not self.text:
            return f'К сожалению произошла ошибка: Делить на нулевое значение нельзя...'
        else:
            return self.text

def devide(x,y):
    if y == 0:
        raise My_Exception
    else:
        return x/y

if __name__ == '__main__':
    # Вывод нашего сообщения
    try:
        result_1 = devide(10,0)
    except My_Exception:
        print(f'Делить на нулевое значение запрещено...')
    else:
        print(f'Результат: {result_1}')
    finally:
        print(f'Программа завершена.\n{"-" * 20}')
    # Вывод ошибки класса
    result_2 = devide(12,0)





