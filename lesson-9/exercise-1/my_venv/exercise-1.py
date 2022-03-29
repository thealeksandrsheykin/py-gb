# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
1.Создать класс TrafficLight (светофор):
    -определить у него один атрибут color (цвет) и метод running (запуск);
    -атрибут реализовать как приватный;
    -в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    -продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
     третьего (зелёный) — на ваше усмотрение;
    -переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    -проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

import time
import sys


class TrafficLight:
    def __init__(self):
        self.__color = ('Yellow','Red','Green')

    def running(self):
        for i,j in enumerate((7,2,10),start=1):
            if self.__check_trafic_light(i) != self.__color[i-1]:
                print(f'Светофор работает некорректно... ' \
                      f'Переключение осуществляется только в указанном порядке ("Red", "Yellow", "Green")')
                return sys.exit(1)
            else:
                print(f'Горит: {self.__color[i-1]}')
                time.sleep(j)

    def __check_trafic_light(self,number):
        my_dict = {1:'Red',2:'Yellow',3:'Green'}
        return my_dict[number]


if __name__ == '__main__':
    my_class = TrafficLight()
    my_class.running()