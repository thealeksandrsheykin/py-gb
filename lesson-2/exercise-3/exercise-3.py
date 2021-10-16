# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного
серьёзнее, чем может сначала показаться.
"""

array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(array):
    try:
        var = int(array[i])
    except ValueError:
        i += 1
        continue
    array.insert(i, '"')
    if array[i+1].isdigit() and len(array[i+1]) < 2:
        array[i+1] = '0' + str(var)
    elif not array[i+1].isdigit() and len(array[i+1]) < 3:
        array[i+1] = array[i+1][0] + '0' + str(var)
    array.insert(i+2, '"')
    i += 3

print(" ".join(array))
