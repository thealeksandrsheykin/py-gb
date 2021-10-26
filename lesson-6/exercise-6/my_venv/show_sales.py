# -*- coding: utf-8 -*-
# !/usr/bin/env python3


import sys
from itertools import islice


def show_sales(start,stop):
    with open('bakery.csv', mode='r') as file:
        for row in islice(file, start, stop):
            print(f'{row.strip()}')

if len(sys.argv[1:]) == 0:
    start, stop = None, None
elif len(sys.argv[1:]) == 1:
    start,stop = list(map(int, sys.argv[1:]))[0],None
    start -= 1
elif len(sys.argv[1:]) == 2:
    start,stop = list(map(int, sys.argv[1:]))
    start -= 1
else:
    sys.exit(1)





show_sales(start,stop)

