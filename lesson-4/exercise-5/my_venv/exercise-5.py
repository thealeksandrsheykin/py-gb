# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""
import sys
from utils import currency_rates

my_dict = currency_rates(sys.argv[1:][0])
print(my_dict)