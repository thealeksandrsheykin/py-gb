# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
5.Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""

import re


class Store:
    def __init__(self):
        self.__store = {}
        self.__department = {}

    def add_to_store(self,equipment):
        # Добавляем на склад оборудование
        self.__store.setdefault(equipment.type_equipment, {model:[]}).append(equipment)
        self.__store[equipment.type_equipment].setdefault(equipment.model, []).append(equipment.series)
        return f'На склад добавлено устройство:\n\t-{equipment}'

    def del_from_store(self,equipment,department=None):
        # Извлекаем со склада оборудование
        model,series = (re.match(r'\S+:\s+(.*)\s+\S+:\s+(.*)', str(equipment))).groups()
        try:
            self.__store[equipment.type_equipment][model].remove(series)
        except (KeyError,ValueError):
            return f'На складе устройство ({equipment}) отсутствует.'
        else:
            if department:
                self.__department.setdefault(department,{})
                self.__department[department].setdefault(equipment.type_equipment,{})
                self.__department[department][equipment.type_equipment].setdefault(model, []).append(series)
            if not self.__store[equipment.type_equipment][model]:
                del self.__store[equipment.type_equipment][model]
            if not self.__store[equipment.type_equipment]:
                del self.__store[equipment.type_equipment]
        return f'Со склада забрали устройство:\n\t-{equipment}'



class Equipments:
    def __init__(self,model,series):
        self.model = model
        self.series = series

    @property
    def type_equipment(self):
        return self.__class__.__name__

    def __repr__(self):
        f'Модель: {self.model} Серия: {self.series}'

class Printer(Equipments):
    def __init__(self,model,series):
        super().__init__(model,series)

    def action(self):
        return f'Принтер {self.model} {self.series} печатает.'

    def __str__(self):
        return f'Модель: {self.model} Серия: {self.series}'


class Scanner(Equipments):
    def __init__(self,model,series):
        super().__init__(model,series)

    def action(self):
        return f'Сканер {self.model} {self.series} сканирует.'

    def __str__(self):
        return f'Модель: {self.model} Серия: {self.series}'


class Xerox(Equipments):
    def __init__(self,model,series):
        super().__init__(model,series)

    def action(self):
        return f'Ксерокс {self.model} {self.series} делает копию.'

    def __str__(self):
        return f'Модель: {self.model} Серия: {self.series}'


if __name__ == '__main__':

    store = Store()
    equipment_1 = Printer('HP', 'Laser 107WR 209U7A')
    store.add_to_store(equipment_1)
    store.del_from_store(equipment_1,'IT')

