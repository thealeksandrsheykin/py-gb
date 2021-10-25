# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
1.Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)—получить список кортежей
 вида:
 (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""
import requests
from operator import itemgetter

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

responce = requests.get(URL).text
my_list_1 = [itemgetter(0,5,6)(i.split()) for i in responce.split('\n') if i != '']

with open(r'nginx_logs.txt', 'r') as file:
    my_list_2 = [itemgetter(0,5,6)(i.split()) for i in (file.read()).split('\n')]

for i,j in enumerate(my_list_1):
    print(f'MY_LIST_1: {my_list_1[i]}\n'
          f'MY_LIST_2: {my_list_2[i]}')



