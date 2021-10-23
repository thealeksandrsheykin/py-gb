# -*- coding: utf-8 -*-
# !/usr/bin/env/ python3

"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя
Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{ "А": { "П": ["Петр Алексеев"] },
  "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] }
}

"""
from time import perf_counter


def thesaurus_adv_1(*args):
    my_dict = dict()
    for i in list(args):
        full_name = i.strip().title()
        name, family = full_name.split()
        if not my_dict.get(family[0], False):
            my_dict[family[0]] = {name[0]: [full_name]}
        elif not my_dict[family[0]].get(name[0], False):
            my_dict[family[0]][name[0]] = [full_name]
        else:
            my_dict[family[0]][name[0]].append(full_name)
    return my_dict


def thesaurus_adv_2(*args):
    my_dict = dict()
    for i in args:
        name, surname = i.split()
        my_dict.setdefault(surname[0], {})
        my_dict[surname[0]].setdefault(name[0], [])
        my_dict[surname[0]][name[0]].append(i)
    return my_dict


#
#     # sort example
#     sorted_dict = {x: out_dict[x] for x in sorted(out_dict)}  # Dict Comprehensions
start_1 = perf_counter()
my_dict_1 = thesaurus_adv_1("Иван Сергеев","Инна Серова","Петр Алексеев","Илья Иванов","Анна Савельева")
print(f'Время выполнения Func-1: {perf_counter() - start_1}')
start_2 = perf_counter()
my_dict_2 = thesaurus_adv_2("Иван Сергеев","Инна Серова","Петр Алексеев","Илья Иванов","Анна Савельева")
print(f'Время выполнения Func-2: {perf_counter() - start_2}')
my_dict_2_sort = {i: my_dict_2[i] for i in sorted(my_dict_2)}
print(f'\n'
      f'Словарь Func-1:\n'
      f'{my_dict_1}\n'
      f'Словарь Func-2:\n'
      f'{my_dict_2}\n'
      f'Сортировка Func-1:\n'
      f'{dict(sorted(my_dict_1.items(), key=lambda item: item[0]))}\n'
      f'Сортировка Func-2:\n'
      f'{my_dict_2_sort} \n')
