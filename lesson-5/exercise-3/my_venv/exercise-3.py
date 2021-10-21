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

from itertools import zip_longest

def my_gen(tutors, klasses):
    for i in range(0,len(tutors)):
        try:
            yield (tutors[i],klasses[i])
        except IndexError:
            yield (tutors[i],None)


tutors  = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Александр','Юлия', 'Мария']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_1 = my_gen(tutors,klasses)
print(type(gen_1))

for i in range(0,len(tutors)):
    print(next(gen_1))

print('-----------------------')

gen_2 = (i for i in zip_longest(tutors,klasses))
print(type(gen_2))

for i in range(0,len(tutors)):
    print(next(gen_2))



