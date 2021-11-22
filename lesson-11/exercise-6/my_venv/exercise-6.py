# -*-coding: utf-8 -*-
# !/usr/bin/env python3

"""
Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

from abc import abstractmethod


class WrongParameter(Exception):
    def __init__(self,msg):
        self.msg =msg
class Store:

    def __init__(self):

        self.store = {'Printer':{},'Scanner':{},'Xerox':{}}
        self.amount = 0

    @property
    def _amount(self):
        return self.amount

    @_amount.setter
    def _amount(self,value):
        if isinstance(value,str):
            raise WrongParameter('Кол-во оборудования  не должно быть строковым значением...')
        else:
            self.amount = value


    def receive(self, device, amount):
        self._amount = amount
        tmp_dict = self.store[device.type]    #cls._store[device.type]
        company, model, series = str(device).split()
        for i in (company, model):
            tmp_dict = tmp_dict.setdefault(i, {})
        tmp_dict.setdefault(series, amount)
        print(f'Cклад получил оборудование {device.type}: {company} {model} {series} - {self.amount} шт.')

    def transfer(self, device, amount, target):
        self._amount = amount
        tmp_dict = self.store[device.type]
        company, model, series = str(device).split()
        try:
            if self.amount > tmp_dict[company][model][series]:
                raise ValueError
        except (KeyError, ValueError):
            print(f'Оборудование {device.type}: {company} {model} {series} отсутсвует или нет в таком кол-ве на складе.')
        else:
            tmp_dict[company][model][series] -= self.amount
            if tmp_dict[company][model][series] == 0:
                del tmp_dict[company][model][series]
            if not tmp_dict[company][model]:
                del tmp_dict[company][model]
            if not tmp_dict[company]:
                del tmp_dict[company]
            print(f'Склад выдал ({device.type}): {company} {model} {series} - {self.amount} шт. --> {target} отделу.')
            return (device, self.amount)

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
    store.receive(printer_1,4)
    store.receive(printer_2,1)
    store.transfer(printer_1,2,'IT')
    store.transfer(printer_1,2, 'MANAGERS')


