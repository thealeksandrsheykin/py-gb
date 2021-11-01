# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
2.*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 --[17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?

"""

import re
import requests

def ParseUrl(data):
    my_list =list()
    regex_ipv4 = r'((?:\d+[\.]){3}\d+)(?:\s+\-){2}\s+\[(.*)\]\s+\"(\w+)\s+(\S+)\s+\S+\"\s+(\w+)\s+(\w+)\s+.*'
    regex_ipv6 = r'((?:\w+[\:]{1,2}){1,7}\w+)(?:\s+\-){2}\s+\[(.*)\]\s+\"(\w+)\s+(\S+)\s+\S+\"\s+(\w+)\s+(\w+)\s+.*'
    for i in data.split('\n'):
        match_ipv4 = re.match(regex_ipv4, i)
        match_ipv6 = re.match(regex_ipv6, i)
        if match_ipv4:
           my_list.append(match_ipv4.groups())
        elif match_ipv6:
            my_list.append(match_ipv6.groups())
        else:
            pass
    return my_list

if __name__ == '__main__':
    url = r'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    response = requests.get(url)
    for i in ParseUrl(response.text):
        print(f'{i}')




