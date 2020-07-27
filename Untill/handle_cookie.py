# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 19:48
# @Author  : xuzengming
# @FileName: handle_cookie.py.py
# @Software: PyCharm

#获取cookie
#写入cookie
#是否携带
from Untill.handle_json import get_Jsonvalue,read_json,write_value
from Untill.handle_ini import handle_init
cookie_json_path = handle_init.get_Inivalue('cookie','mock')
def get_cookie_value(cookie_key):
    '''
    获取到cookie.json中指定的cookie串
    :param cookie_key:指定串的键
    :return:cookie串
    '''
    data = read_json(cookie_json_path)
    return data[cookie_key]

def write_cookie(data,cookie_key):
    '''
    获取到cookie.json中指定的cookie串，将指定的串替换为data，起到一个更新cookie.json的作用
    :param data:获取到的cookie
    :param cookie_key:用于指定cookie.json的部分串
    :return:
    '''
    data1 = read_json(cookie_json_path)
    data1[cookie_key] = data
    write_value(cookie_json_path,data1)


if __name__ == '__main__':
    data = {
        "aaaa":"1111111111111111"
    }
    print(write_cookie(data,'web'))