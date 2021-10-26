# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
2.*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""

import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

responce = requests.get(URL).text
my_list_1 = [i.split()[0] for i in responce.split('\n') if i != '']

my_dict = {i: my_list_1.count(i) for i in set(my_list_1)}
my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

for i,j in enumerate(list(my_dict.keys())[:5],1):
    print(f'IP адрес спамера #{i}: {j:15} количество отправленных им запросов: {my_dict[j]}')

