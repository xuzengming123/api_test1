#coding=utf-8
import json
import os
from Untill.handle_ini import handle_ini

def read_json(JsonFilePath):
    '''
    加载
    :JsonFilePath:读取的文件路径，
    :return:
    '''
    with open(JsonFilePath,encoding='UTF-8') as f:
        data = json.load(f)
    return data

def get_Jsonvalue(JsonFilePath,key):
    '''
    获取json文件的值
    :param key:
    :return: value
    '''
    data = read_json(JsonFilePath)
    if key:
        return data.get(key)
    else:
        return None

# DataPath = handle_ini.get_Jsonvalue('user_data','mock')
# print(get_value(DataPath,'/api3/getbanneradvertver2'))