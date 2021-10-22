#-*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3. Есть два списка:

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
(<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.

"""
import sys
from time import perf_counter
from itertools import zip_longest

def my_gen(tutors, klasses):
    for i in range(0,len(tutors)):
        try:
            yield (tutors[i],klasses[i])
        except IndexError:
            yield (tutors[i],None)


tutors  = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Александр','Юлия', 'Мария']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

start = perf_counter()
gen_1 = my_gen(tutors,klasses)
print(f'''
Время создания GEN_1: {perf_counter()-start}
Тип объекта GEN_1: {type(gen_1)}.
Генератор GEN_1 занимет в памяти: {sys.getsizeof(gen_1)}
''')


for i in range(0,len(tutors)):
    print(next(gen_1))

print(f'{24 * "-"}')

start = perf_counter()
gen_2 = (i for i in zip_longest(tutors,klasses))
print(f'''
Время создания GEN_2: {perf_counter() -start}
Тип объекта GEN_2: {type(gen_2)}.
Генератор GEN_2 занимет в памяти: {sys.getsizeof(gen_2)}
''')

for i in range(0,len(tutors)):
    print(next(gen_2))



