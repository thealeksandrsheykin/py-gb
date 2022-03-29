#-*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
3.Реализовать базовый класс Worker (работник):
    -определить атрибуты: name, surname, position (должность), income (доход);
    -последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
     например: {"wage": wage, "bonus": bonus};
    -создать класс Position (должность) на базе класса Worker;
    -в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
     (get_total_income);
    -проверить работу примера на реальных данных:
            создать экземпляры класса Position,
            передать данные,
            проверить значения атрибутов,
            вызвать методы экземпляров.
"""

class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position # должность
        self._income = {"wage": wage, "bonus": bonus}    # доход (оклад, премия)

class Position(Worker):
    def __init__(self,name,surname,position,wage,bonus):
        super().__init__(name,surname,position,wage,bonus)

    def get_full_name(self):
        return f'{(self.name).capitalize()} {(self.surname).capitalize()}'

    def get_total_income(self):
        return sum(self._income.values())



if __name__ == '__main__':
    my_class = Position('иван','сидоров','менеджер',100,20)
    print(f'Name:     {my_class.name}\n'
          f'Surname:  {my_class.surname}\n'
          f'Position: {my_class.position}\n'
          f'Income:   {my_class._income}\n')

    print(f'Полное имя сотрудника: {my_class.get_full_name()}')
    print(f'Доход с учётом премии: {my_class.get_total_income()}')




