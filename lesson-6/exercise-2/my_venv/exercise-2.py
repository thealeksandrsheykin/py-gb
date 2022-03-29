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

count = 0
spammer = ''
for i in set(my_list_1):
    if my_list_1.count(i) > count:
        count = my_list_1.count(i)
        spammer = i
    else:
        continue

print(f'IP адрес спамера: {spammer} количество отправленных им запросов: {count}')

