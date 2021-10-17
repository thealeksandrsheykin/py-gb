# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:

[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например  «5
руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек
или 0 копеек (должно быть 07 коп или 00 коп). Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же). Создать новый список, содержащий те же цены,
но отсортированные по убыванию. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих  товаров по
возрастанию, написав минимум кода?
"""

my_list = [57.08, 46.51, 97, 1.2, 100.32, 67.09, 87.91, 24, 12.42, 71.12]

# Выводим цены в строку по шаблону «0 руб 00 коп»
for i in my_list:
    rub = int(i)
    kop = int(round(i - int(i), 2) * 100)
    if len(str(kop)) < 2:
        kop = '0' + str(kop)
    print(f'"{rub} руб {kop} коп";', end=' ')
print(f'\n')

# Отсортировать список по возрастанию не создавая новый список  и доказать что объект списка после сортировки
# остался тот же
print(f'Исходный список: {my_list}')
print(f'Адрес памяти  для объекта 57.08: {id(my_list[0])}')
my_list.sort()
print(f'Отсортированный список: {my_list}')
print(f'Адрес памяти  для объекта 57.08: {id(my_list[4])}')

# Создать новый список отсортированный по убыванию
my_list_2 = sorted(my_list, reverse=True)

# Вывести цены пяти самых дорогих товаров по возрастанию
print(f'Пять самых дорогих товаров: {my_list_2[:-5][::-1]}')