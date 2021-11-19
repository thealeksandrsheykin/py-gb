# -*-coding: utf-8 -*-
# !/usr/bin/env python3

"""
Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

from abc import abstractmethod

class CheckParameters:

    def __set__(self, instance, value):
        print(value)
        if isinstance(value,int):
            setattr(instance,self.tmp_name,value)
        else:
            raise ValueError

    def __set_name__(self, owner, name):
        self.tmp_name = '_' + name
        print(self.tmp_name)

    def __get__(self, instance, owner):
        return instance._amount


class Store:

    _STORE = {'Printer':{},'Scanner':{},'Xerox':{}}
    _AMOUNT = CheckParameters()

    def __init__(self):
        self.store = Store._STORE
        self.amount = Store._AMOUNT

    @classmethod
    def receive(cls, device, amount):
        cls._AMOUNT = amount
        tmp_dict = cls._STORE[device.type]    #cls._store[device.type]
        company, model, series = str(device).split()
        for i in (company, model):
            tmp_dict = tmp_dict.setdefault(i, {})
        tmp_dict.setdefault(series, amount)
        print(f'Cклад получил оборудование {device.type}: {company} {model} {series} - {amount} шт.')

    def transfer(self, device, amount, target):
        tmp_dict = self._store[device.type]
        company, model, series = str(device).split()
        try:
            if amount > tmp_dict[company][model][series]:
                raise ValueError
        except (KeyError, ValueError):
            return f'Оборудование {device.type}: {company} {model} {series} отсутсвует или нет в таком кол-ве на складе.'
        else:
            tmp_dict[company][model][series] -= amount
            if tmp_dict[company][model][series] == 0:
                del tmp_dict[company][model][series]
            if not tmp_dict[company][model]:
                del tmp_dict[company][model]
            if not tmp_dict[company]:
                del tmp_dict[company]
            print(f'Склад выдал ({device.type}): {company} {model} {series} - {amount} шт. --> {target} отделу.')
            return (device, amount)

    def qty(self,device):
        tmp_dict = self._store[device.type]
        company, model, series = str(device).split()
        try:
            return tmp_dict[company][model][series]
        except:
            return 0


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
    printer_1 = Printer('HP','LaserJet', 'P1006')
    printer_2 = Printer('HP','LaserJet', 'P1007')
    store.receive(printer_1,2)
    store.receive(printer_2,'rt')
