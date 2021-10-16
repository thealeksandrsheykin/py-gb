# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
    до минуты: <s> сек;
    до часа: <m> мин <s> сек;
    до суток: <h> час <m> мин <s> сек;
    * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = int(input("Введите продолжительность в секундах: "))

# Высчитываем секунды
seconds = duration % 60
# Вычисляем количество минут в введенной продолжительности
num_min = duration // 60
# Высчитываем минуты
minutes = num_min % 60
# Вычисляем количество часов в введенной продолжительности
num_hour = num_min // 60
# Высчитываем часы
hours = num_hour % 24
# Высчитываем дни
days = num_hour // 24

# Можно выводить всегда все
# print("{} дн {} час {} мин {} сек".format(days, hours, minutes, seconds))

# Можно выводить через условие
if days == 0 and hours != 0:
    print("{} час {} мин {} сек".format(hours, minutes, seconds))
elif days == 0 and hours == 0 and minutes != 0:
    print("{} мин {} сек".format(minutes, seconds))
elif days == 0 and hours == 0 and minutes == 0:
    print("{} сек".format(seconds))
else:
    print("{} дн {} час {} мин {} сек".format(days, hours, minutes, seconds))
