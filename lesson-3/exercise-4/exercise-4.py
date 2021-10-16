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


def thesaurus_adv(*args):
    my_dict = dict()
    for i in list(args[0].split(',')):
        full_name = i.strip().title()
        name, family = full_name.split()
        if not my_dict.get(family[0], False):
            my_dict[family[0]] = {name[0]: [full_name]}
        elif not my_dict[family[0]].get(name[0], False):
            my_dict[family[0]][name[0]] = [full_name]
        else:
            my_dict[family[0]][name[0]].append(full_name)
    return my_dict


data = input('Введите «Имя Фамилия» через запятую: ')

print(f'''
Словарь:
{thesaurus_adv(data)}

Словарь отсортированный по первой букве фамилии:
{dict(sorted(thesaurus_adv(data).items(), key=lambda item: item[0]))}
''')
