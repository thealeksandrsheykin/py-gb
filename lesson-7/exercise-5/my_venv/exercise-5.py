# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5.*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а
значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

"""

import os


path = r'..\\'
my_list = [100,1000,10000,100000]
my_dict = dict.fromkeys(my_list,None)
tmp_dict = dict.fromkeys(my_list,0)

for root, dirs,files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            ext = os.path.splitext(filepath)[-1].lstrip('.')
            size = os.stat(filepath).st_size
            try:
                key = min(filter(lambda i: size < i, my_list))
            except ValueError:
                pass
            tmp_dict[key] += 1

print(tmp_dict)











