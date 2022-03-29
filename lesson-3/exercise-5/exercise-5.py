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


def get_jokes_1(number, repeats=True):
    my_list1 = list()
    my_list2 = list()
    # Делаем цикл на количество необходимы шуток
    for i in range(0, number):
        joke = ''
        for j in [nouns, adverbs, adjectives]:
            # Рандомно забираем одно слово из каждого списка и присваиваем к переменной тем самым составляя предложение
            if not repeats:
                if number > min(len(nouns), len(adverbs), len(adjectives)):
                    return 'No way'
                else:
                    # Если флаг = True, то каждое слово выбранное рандомно добавляем в список чтобы далее
                    # сравнивать с ним
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


def get_jokes_2(number, repeats=True):
    my_list = []
    if not repeats:
        if number > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(number):
                my_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(number):
            cur_nouns = random.choice(nouns)
            cur_adverbs = random.choice(adverbs)
            cur_adjectives = random.choice(adjectives)
            my_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return my_list


print(f'{get_jokes_1(4, repeats=False)}')
print(f'{get_jokes_2(5, repeats=True)}')
