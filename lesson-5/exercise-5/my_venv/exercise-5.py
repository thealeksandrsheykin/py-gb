# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""
import sys
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = list()
start = perf_counter()
for i in src:
    if src.count(i) == 1:
        result.append(i)
    else:
        continue
print(f'''
Время выполнения: {perf_counter()-start}
Список занимает в памяти: {sys.getsizeof(result)}
Результат: {result}''')

print(f'{24*"-"}')
result = list()

start = perf_counter()
result = [i for i in src if src.count(i) == 1]
print(f'''
Время выполнения: {perf_counter()-start}
Список занимает в памяти: {sys.getsizeof(result)}
Результат: {result}''')