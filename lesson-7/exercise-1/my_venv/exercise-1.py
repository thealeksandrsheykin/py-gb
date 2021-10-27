# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

"""

import os
import json

path = os.getcwd()
print(f'Рабочий каталог: {path}')

# Прямой способ решения данной задачи
"""
folder = 'my_project'
subfolders = ('settings', 'mainapp', 'adminapp', 'authapp')

for i in subfolders:
    dir_path = os.path.join(folder, i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
"""

# Забираем структуру данных из файла JSON
with open('structura.json', 'r') as file:
    my_dict = json.load(file)
    for key,value in my_dict.items():
        if not os.path.exists(value['path']):
            os.makedirs(value['path'])

