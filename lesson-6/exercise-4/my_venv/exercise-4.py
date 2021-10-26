# -*- config: utf-8 -*-
# !/usr/bin/env python3


"""
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально
создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно создавать словарь с данными.
Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел
после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""


import sys
from itertools import zip_longest

with open('users_hobby.txt', mode= 'w', encoding='utf-8') as file:
    with open('users.csv', mode='r', encoding='utf-8') as users:
        users_num= sum(1 for _ in users)
        with open('hobby.csv', mode='r', encoding='utf-8') as hobby:
            hobby_num = sum(1 for _ in hobby)
            if users_num < hobby_num:
                sys.exit(1)
            else:
                users.seek(0)
                hobby.seek(0)
                for i,j in zip_longest(users,hobby):
                    file.write(f"{' '.join(i.strip().split(','))}: {j}")
