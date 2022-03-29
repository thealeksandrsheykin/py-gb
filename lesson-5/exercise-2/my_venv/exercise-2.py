# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

odd_to_15 = (num for num in range(1,16,2))
print(type(odd_to_15))
