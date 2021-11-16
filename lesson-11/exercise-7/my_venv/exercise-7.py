# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
7.Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов
сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
"""


class Complex:
    def __init__(self,complex):
        self.complex = complex

    def __add__(self, other):
        if isinstance(self.complex and other.complex, complex):
            return self.complex + other.complex
        else:
            return None

    def __mul__(self, other):
        if isinstance(self.complex and other.complex, complex):
            return self.complex * other.complex
        else:
            return None

if __name__ == '__main__':
    x = Complex(1+2j)
    y = Complex(3+7j)
    print(f'Сложение: {x + y}')
    print(f'Умножение: {x * y}')

