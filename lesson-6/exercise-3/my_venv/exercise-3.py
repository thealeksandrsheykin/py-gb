# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре
значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import sys
import json

with open(r'users.csv', 'r', encoding='utf-8') as u, open(r'hobby.csv', 'r', encoding='utf-8') as h:
    users = u.readlines()
    hobby = h.readlines()

my_dict = dict()
if len(users) < len(hobby):
    sys.exit(1)
else:
    for i in range(0,len(users)):
        key = ' '.join(users[i].strip('\n').split(','))
        try:
            value = hobby[i].strip('\n')
        except IndexError:
            value = None
        my_dict[key] = value

# Записываем словарь в json file
with open('users_hobby.json', 'w', encoding='utf-8') as file:
    json.dump(my_dict,file, ensure_ascii=False, indent=2)

# Читаем json file
with open ('users_hobby.json', 'r', encoding='utf-8') as file:
    json_file = json.load(file)

for key,value in json_file.items():
    print(f'{key} -> {value}')




