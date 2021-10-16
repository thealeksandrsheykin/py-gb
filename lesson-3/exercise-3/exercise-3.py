# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:

thesaurus("Иван", "Мария", "Петр", "Илья")
{ "И": ["Иван", "Илья"], "М": ["Мария"], "П": ["Петр"] }

Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли
использовать словарь в этом случае?
"""


def thesaurus(*args):
    my_dict = dict()
    for i in list(args[0].split(',')):
        name = i.strip().lower()
        if not my_dict.get(name[0], False):
            my_dict[name[0]] = [name]
        else:
            my_dict[name[0]].append(name)
    return my_dict


data = input("Введите имена сотрудников через запятую: ")
print(f'{thesaurus(data)}')

# Отсортировать словарь по ключу
print(f'{dict(sorted(thesaurus(data).items(), key=lambda item: item[0]))}')