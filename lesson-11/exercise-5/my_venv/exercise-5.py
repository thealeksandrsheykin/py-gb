# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5.Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""

from abc import abstractmethod

class Store:

    def __init__(self):
        self.__store = {'Printer':{},'Scanner':{},'Xerox':{}}

        self.departments = {'IT':{'Printer':[],'Scanner':[],'Xerox':[]},
                            'Managers':{'Printer':[],'Scanner':[],'Xerox':[]}}

    def add_to_store(self,equipment,qty):
        model,series = str(equipment).split(':')
        self.__store[equipment.type_eq].setdefault(model,{})
        self.__store[equipment.type_eq][model].setdefault(series,0)
        self.__store[equipment.type_eq][model][series] += qty
        return f'На склад добавлен {equipment.type_eq}: {model} {series} {qty} шт.'

    def del_to_store(self,equipment,department,qty=1):
        model,series = str(equipment).split(':')
        try:
            self.__store[equipment.type_eq][model][series]
        except KeyError:
            return f'На складе {equipment.type_eq}: {model} {series} не обнаружен.'
        else:
            self.__store[equipment.type_eq][model][series] -= qty
            if self.__store[equipment.type_eq][model][series] == 0:
                del self.__store[equipment.type_eq][model][series]
            if not self.__store[equipment.type_eq][model]:
                del self.__store[equipment.type_eq][model]
            self.departments[department][equipment.type_eq].append(str(equipment))

        return f'Со склада забрали {equipment.type_eq}: {model} {series} {qty} шт. в {department} отдел.'


class Equipments:

    def __init__(self,model,series):
        self.model = model
        self.series = series

    @property
    def type_eq(self):
        return self.__class__.__name__

    @abstractmethod
    def action(self):
        pass

    def __repr__(self):
        return f'{self.model}:{self.series}'

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
    store = Store()
    printer = Printer('HP','LaserJet P1006')
    printer_2 = Printer('Epson', 'Test 1001')
    printer_3 = Printer('Epson', 'Test 1002')
    scanner = Scanner('Epson','WorkForce DS-1630')
    xerox = Xerox('Canon','PIXMA MG2540S')

    print(store.add_to_store(printer,2))
    print(store.add_to_store(printer,4))
    print(store.add_to_store(printer_2, 5))
    print(store.add_to_store(printer_3, 1))
    print(store.del_to_store(printer,'IT',2))
    print(store.del_to_store(printer_3, 'Managers', 1))







