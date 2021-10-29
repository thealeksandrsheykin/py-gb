# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html


Примечание: исходные файлы необходимо оставить;
обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
(Пространство имён позволяет отличить один элемент от другого, когда они имеют одинаковое название, но принадлежат разным
пространствам имён.)

предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
"""

import os
import shutil

path = r'.\my_project'

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".html"):
            src = '\\'.join(root.split('\\')[:-1])
            dst = os.path.join(path,'templates')
            shutil.copytree(src,dst,dirs_exist_ok=True,ignore=shutil.ignore_patterns('*.txt','dir_for_ignore'))



