# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
1.Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31  22              3   5   32              3   5   8   3
37  43              2   4   6               8   3   7   1
51  86              -1  64  -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.
"""

class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    @property
    def size(self):
        col = 0
        for row,columns in enumerate(self.matrix,start=1):
            if col != 0 and col != len(columns):
                raise ValueError('Error...')
            col = len(columns)
        return (row,col)

    def __add__(self, other):
        result = list()
        if self.size == other.size:
           for row in range(len(self.matrix)):
               result.append([i + j for i, j in zip(self.matrix[row], other.matrix[row])])
        else:
            raise ValueError('Error...')
        return Matrix(result)


if __name__ == '__main__':
    my_class_1 = Matrix([[3,5,32],[2,4,6],[-1,64,-8]])
    my_class_2 = Matrix([[25,1,-9],[4,5,0],[100,9,-24]])
    print(f'Матрица 1:\n{my_class_1}\nРазмер матрицы: {my_class_1.size}\n')
    print(f'Матрица 2:\n{my_class_2}\nРазмер матрицы: {my_class_2.size}\n')
    print(f'Результат сложения матриц:\n{my_class_1+my_class_2}')

