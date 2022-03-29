# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```
Подсказка: использовать возможности python, изученные на уроке.
"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = list()
for i in range(1,len(src)):
    if (src[i] > src[i-1]):
        result.append(src[i])
print(result)

print(f'{24 * "-"}')

result = list()
result = [src[i] for i in range(1,len(src)) if src[i] > src[i-1]]
print(result)
