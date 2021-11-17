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
        self.store = {'Printer':{},'Scanner':{},'Xerox':{}}
        self.depts = {'IT' :{'Printer':{},'Scanner':{},'Xerox':{}},
                      'MGR':{'Printer':{},'Scanner':{},'Xerox':{}}}


    def add_to(self,device,qty,to=None):   # Добавление устройств в различные подразделения (по умолчанию на склад)
        if to is None:
            to = self.store
        to[device.type].setdefault(device.company,{})                              # Компания устройства
        to[device.type][device.company].setdefault(device.model,{})                # Модель устройства
        to[device.type][device.company][device.model].setdefault(device.series, 0) # Серия устройства
        to[device.type][device.company][device.model][device.series] += qty
        return f'На склад добавлен {device.type}: {device.company} {device.model} {device.series} {qty} шт.'


    def transfer_from_to(self,device,qty,dst):
        try:
            amount = self.store[device.type][device.company][device.model][device.series]
        except KeyError:
            return f'{device.type}: {device.company} {device.model} {device.series} не обнаружен.'
        else:
            if amount < qty:
                return f'Такого количества {device.type}: {device.company} {device.model} {device.series} нет.'
            else:
                self.store[device.type][device.company][device.model][device.series] -= qty
                self.add_to(device,qty, self.depts[dst]) # Передаем со склада в подразделение
                if (amount - qty) == 0:
                    del self.store[device.type][device.company][device.model][device.series]
                if not self.store[device.type][device.company][device.model]:
                    del self.store[device.type][device.company][device.model]
                if not self.store[device.type][device.company]:
                    del self.store[device.type][device.company]
        return f'{device.company} {device.model} {device.series} {qty} шт. перемещен СКЛАД --> {dst} '





        return f'Со склада забрали {device.type}: {device.model} {device.series} {qty} шт. в {dept} отдел.'

    def __check_amount(self):
        if self.__store[equipment.type_eq][model][series] == 0:
            del self.__store[equipment.type_eq][model][series]
        if not self.__store[equipment.type_eq][model]:
            del self.__store[equipment.type_eq][model]


class Equipments:

    def __init__(self,company,model,series):
        self.company = company
        self.model = model
        self.series = series
        self.type = self.__class__.__name__

    @abstractmethod
    def action(self):
        pass

    def __repr__(self):
        return f'{self.company} {self.model} {self.series}'

class Printer(Equipments):

    def __init__(self,company,model,series):
        super().__init__(company,model,series)

    def action(self):
        return f'Принтер {self.company} {self.model} {self.series} печатает.'

class Scanner(Equipments):

    def __init__(self,company,model,series):
        super().__init__(company,model,series)

    def action(self):
        return f'Сканер {self.company} {self.model} {self.series} сканирует.'

class Xerox(Equipments):

    def __init__(self,company,model,series):
        super().__init__(company,model,series)

    def action(self):
        return f'Ксерокс {self.company} {self.model} {self.series} копирует.'


if __name__ == '__main__':
    store = Store()
    printer = Printer('HP','LaserJet', 'P1006')
    print(store.add_to(printer,6))
    print(store.transfer_from_to(printer,2,'IT'))
    print(store.transfer_from_to(printer,2,'MGR'))
    print(store.depts)
    print(store.store)










