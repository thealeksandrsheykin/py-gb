# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
from fileinput import FileInput


def edit_sales(row, value):
    flag_change = False
    with open('bakery.csv', mode='r+') as file:
        with open('bakery.tmp', mode='w+') as file_temp:
            for i, j in enumerate(file, 1):
                if i == int(row):
                    flag_change = True
                    file_temp.write(f'{value}\n')
                else:
                    file_temp.write(j)
            if not flag_change:
                sys.exit(1)
            file_temp.seek(0)
            file.seek(0)
            for line in file_temp:
                file.write(line)


def edit_sales_adv(row, value):
    flag_change = False
    with FileInput(files='bakery.csv', inplace=True, ) as file:
        for i, j in enumerate(file, 1):
            if i == int(row):
                flag_change = True
                print(f'{value}')
            else:
                print(f'{j.strip()}')
        if not flag_change:
            sys.exit(1)


if len(sys.argv) > 3:
    sys.exit(1)
else:
    row, value = sys.argv[1:]
    # edit_sales(row, value)
    edit_sales_adv(row, value)
