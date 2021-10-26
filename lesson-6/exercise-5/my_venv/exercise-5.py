# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных файлов
и имя выходного файла. Проверить работу скрипта.
"""

import sys
from itertools import zip_longest

users,hobby,result = sys.argv[1:]

with open(result, mode= 'w+', encoding='utf-8') as file:
    with open(users, mode='r', encoding='utf-8') as users:
        users_num= sum(1 for _ in users)
        with open(hobby, mode='r', encoding='utf-8') as hobby:
            hobby_num = sum(1 for _ in hobby)
            if users_num < hobby_num:
                sys.exit(1)
            else:
                users.seek(0)
                hobby.seek(0)
                for i,j in zip_longest(users,hobby):
                    file.write(f"{' '.join(i.strip().split(','))}: {j}")