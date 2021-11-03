# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
4.Реализуйте базовый класс Car:
    -У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
     А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
     повернула (куда);
    -Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    -Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    -Для классов TownCar и WorkCar переопределите метод show_speed.
     При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{(self.color).capitalize()} автомобиль марки "{self.name}" начал движение.'

    def stop(self):
        return f'{(self.color).capitalize()} автомобиль марки "{self.name}" остановился.'

    def turn(self,direction):
        return f'{(self.color).capitalize()} автомобиль марки "{self.name}" повернул {direction}.'

    def show_speed(self):
        return f'Текущая скорость автомобиля "{self.name}" {(self.color).lower()}: {self.speed}км/ч.'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость автомобиля "{self.name}" ({(self.color).lower()}): {self.speed}км\ч. ' \
                   f'(СКОРОСТЬ ПРЕВЫШЕНА!)'
        else:
            return f'Текущая скорость автомобиля "{self.name}" ({(self.color).lower()}): {self.speed}км\ч.'

class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость автомобиля "{self.name}" ({(self.color).lower()}): {self.speed}км\ч. ' \
                   f'(СКОРОСТЬ ПРЕВЫШЕНА!)'
        else:
            return f'Текущая скорость автомобиля "{self.name}" ({(self.color).lower()}): {self.speed}км\ч.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def turn_siren(self,mode):
        if self.is_police:
            return f'Полицейскому автомобилю "{self.name}" ({(self.color).lower()}) поступила команда {mode} сирену.'



if __name__ == '__main__':
    my_class_1 = Car(60,'Черный','BMW',False)
    print(f'1.{my_class_1.go()}\n  {my_class_1.show_speed()}\n  {my_class_1.turn("налево")}\n  {my_class_1.stop()}')
    my_class_2 = TownCar(80,'Белый','KIA',False)
    print(f'2.{my_class_2.go()}\n  {my_class_2.show_speed()}\n  {my_class_2.turn("направо")}\n {my_class_2.stop()}')
    my_class_3 = SportCar(200,'Красный','Ferrari',False)
    print(f'3.{my_class_3.go()}\n  {my_class_3.show_speed()}\n  {my_class_3.turn("налево")}\n  {my_class_3.stop()}')
    my_class_4 = WorkCar(40, 'Желтый', 'Hyundai', False)
    print(f'4.{my_class_4.go()}\n  {my_class_4.show_speed()}\n  {my_class_4.turn("направо")}\n  {my_class_4.stop()}')
    my_class_5 = PoliceCar(100, 'Бело-синий', 'Lada', True)
    print(f'5.{my_class_5.go()}\n  {my_class_5.turn_siren("включить")}\n  {my_class_5.stop()}\n')


