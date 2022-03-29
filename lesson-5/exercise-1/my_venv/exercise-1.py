# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
"""

def odd_nums(max_num):
    for num in range(1,max_num+1,2):
        yield num
max_num = 15
odd_to_15 = odd_nums(max_num)
