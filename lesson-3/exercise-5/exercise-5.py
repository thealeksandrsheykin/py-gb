# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""

5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2) ["лес завтра зеленый", "город вчера веселый"]

Документировать код функции. Сможете ли вы добавить еще
один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только
в одной шутке)? Сможете ли вы сделать аргументы именованными?

"""
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(**kwargs):
    my_list1 = list()
    my_list2 = list()
    # Делаем цикл на количество необходимы шуток
    for i in range(0, kwargs['number']):
        joke = ''
        for j in [nouns, adverbs, adjectives]:
            # Рандомно забираем одно слово из каждого списка и присваиваем к переменной тем самым составляя предложение
            if kwargs['flag']:
                # Если флаг = True, то каждое слово выбранное рандомно добавляем в список чтобы далее сравнивать с ним
                while True:
                    word = random.choice(j)
                    if not (word in my_list2):
                        my_list2.append(word)
                        break
                    else:
                        pass
            else:
                word = random.choice(j)
            joke += f'{word} '
        my_list1.append(joke.rstrip())
    return my_list1


print(f'{get_jokes(number=4, flag=True)}')