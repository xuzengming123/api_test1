# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 11:32
# @Author  : xuzengming
# @FileName: handle_header.py.py
# @Software: PyCharm

from Untill.handle_json import read_json
from Untill.handle_ini import handle_init

def get_header():
    data = read_json(handle_init.get_Inivalue('header','mock'))
    return data

