# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не
программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os
import yaml


def GetPaths(data,paths,root):
    for folder,structures in data.items():
        dirpath = os.path.join(root,folder)
        if structures:
            for files in structures:
                if isinstance(files,dict):
                    GetPaths(files,paths,dirpath)
                else:
                    filepath = os.path.join(dirpath,files)
                    paths.append(filepath)
        else:
            paths.append(f'{dirpath}\\')
    return paths


my_dict = dict()
with open(r'config.yaml', 'r', encoding='utf-8') as file:
    my_dict = yaml.load(file, Loader=yaml.FullLoader)

for i in GetPaths(my_dict,list(),os.getcwd()):
    if not os.path.exists(os.path.dirname(i)):
        os.makedirs(os.path.dirname(i))
    if os.path.isfile(i):
        with open(i, "w") as file:
            pass

