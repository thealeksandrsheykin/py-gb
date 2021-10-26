# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
import csv

def add_sale(summa):
    with open('bakery.csv', mode='a+', newline='') as file_write:
        writer = csv.writer(file_write, delimiter=';', lineterminator='\n')
        writer.writerow([summa])

if len(sys.argv) > 2:
    sys.exit(1)
else:
    add_sale(sys.argv[1])
