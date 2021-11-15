# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
4.Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""

class Store:
    def __init__(self):
        self.__store = {}

    def add_to_store(self,equipment):
        # Добавляем на склад оборудование
        self.__store.setdefault(equipment.type_equipment, {})
        self.__store[equipment.type_equipment].setdefault(equipment.model, []).append(equipment.series)
        return f'На склад добавлено устройство:\n\t-Модель: {equipment.model}\n\t-Cерия:  {equipment.series}\n'

    def get_from_store(self,equipment):
        # Извлекаем со склада оборудование
        series_list = self.__store[equipment.type_equipment].setdefault(equipment.model)
        try:
            series_list.pop(series_list.index(equipment.series))
        except (AttributeError,ValueError):
            return f'На складе не найдено оборудования такой модели и серии...'
        else:
            if series_list == []: # Удаляем модель, если на складе больше ее нет
               del self.__store[equipment.type_equipment][equipment.model]
            if self.__store[equipment.type_equipment] == {}: # Если склад пустой,удаляем все категории оборудования
                del self.__store[equipment.type_equipment]
        return f'Со склада забрали устройство:\n\t-Модель: {equipment.model}\n\t-Cерия:  {equipment.series}\n'

    def __str__(self):
        result = f'{24 * "-"}\n'
        for equipment in self.__store:
            result += f'{equipment}:'
            for i, j in self.__store[equipment].items():
                result += "\n\t{}:\n\t\t{}\n".format(i, '\n\t\t'.join(j))
        result += f'\n{24 * "-"}'
        return result


class Equipments:
    def __init__(self,model,series):
        self.model = model
        self.series = series

    @property
    def type_equipment(self):
        return self.__class__.__name__

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
    equipment_2 = Printer('HP', 'Neverstop Laser 1000w')
    equipment_3 = Scanner('Epson', 'WorkForce DS-530')
    equipment_4 = Scanner('Canon', 'ImageFormula DR-C130')
    equipment_5 = Xerox('Brother', 'DCP-1602R')
    equipment_6 = Xerox('Kyocera', 'Ecosys M2735dn')

    store.add_to_store(equipment_1)
    store.add_to_store(equipment_2)
    store.add_to_store(equipment_3)
    store.add_to_store(equipment_4)
    store.add_to_store(equipment_5)
    store.add_to_store(equipment_6)

    print(store)
    store.get_from_store(equipment_5)
    store.get_from_store(equipment_6)
    print(store)


