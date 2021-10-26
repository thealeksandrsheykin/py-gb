# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
from fileinput import FileInput


def edit_sales(row,value):
    with open('bakery.csv', mode='rt+') as file:
        file_position = 0
        for i,j in enumerate(file,start=1):
            if i == int(row):
                break
            else:
                file_position += len(j)
        print(file_position)
        file.seek(file_position)
        file.write('\n')


if len(sys.argv) > 3:
    sys.exit(1)
else:
    row,value = sys.argv[1:]
    edit_sales(row,value)
