# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
4.Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""

from abc import abstractmethod

class Store:

    def __init__(self):
        self.__store = {}

    def add_to_store(self):
        pass

    def del_to_store(self):
        pass

class Equipments:

    def __init__(self,model,series):
        self.model = model
        self.series = series

    @abstractmethod
    def action(self):
        pass

class Printer(Equipments):

    def __init__(self,model,series):
        super().__init__(model,series)

    def action(self):
        return f'Принтер {self.model} ({self.series}) печатает.'

class Scanner(Equipments):

    def __init__(self,model,series):
        super().__init__(model,series)

    def action(self):
        return f'Сканер {self.model} ({self.series}) сканирует.'

class Xerox(Equipments):

    def __init__(self,model,series):
        super().__init__(model,series)

    def action(self):
        return f'Ксерокс {self.model} ({self.series}) копирует.'


if __name__ == '__main__':
    printer = Printer('HP','LaserJet P1006')
    scanner = Scanner('Epson','WorkForce DS-1630')
    xerox = Xerox('Canon','PIXMA MG2540S')
    print(f'{printer.action()}\n'
          f'{scanner.action()}\n'
          f'{xerox.action()}')
