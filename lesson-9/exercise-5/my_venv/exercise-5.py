# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5. Реализовать класс Stationery (канцелярская принадлежность):
        -определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
        -создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
        -в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
        сообщение;
        -создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""

class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


if __name__ == '__main__':
    my_class_1 = Stationery('')
    print(my_class_1.draw())
    my_class_2 = Pen('ручкой')
    print(my_class_2.draw())
    my_class_3 = Pen('ручкой')
    print(my_class_3.draw())
    my_class_4 = Handle('маркером')
    print(my_class_4.draw())