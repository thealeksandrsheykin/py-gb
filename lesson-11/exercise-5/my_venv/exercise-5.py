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
        self._store = {'Printer':{},'Scanner':{},'Xerox':{}}

    def receive(self, device, amount):
        tmp_dict = self._store[device.type]
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
    scanner_1 = Scanner('EPSON', 'Perfection', 'V600')
    scanner_2 = Scanner('EPSON', 'Expression', '12000XL')
    xerox_1 = Xerox('Canon', 'Super', '3600KL')
    xerox_2 = Xerox('Xerox', 'Standart', 'B1025DNA')
    print(f'{printer_2.action()}\n'
          f'{scanner_2.action()}\n')
    store.receive(printer_1, 4)
    store.receive(scanner_1, 6)
    store.receive(xerox_1, 2)
    print(f'\nКол-во принтеров 1 на складе: {store.qty(printer_1)}\n'
          f'Кол-во принтеров 2 на складе: {store.qty(printer_2)}\n')
    store.transfer(scanner_1,4,'MANAGERS')
    store.transfer(xerox_1, 2,'ACCOUNT')
    store.transfer(printer_1,2,'IT')
    print(f'\nКол-во сканеров 1 на складе: {store.qty(scanner_1)}\n'
          f'Кол-во ксероксов 1 на складе: {store.qty(xerox_1)}\n'
          f'Кол-во принтеров 1 на складе: {store.qty(printer_1)}\n')










