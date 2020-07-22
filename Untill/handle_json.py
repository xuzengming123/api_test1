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

def write_value(file_path,data):
    data_value = json.dumps(data)
    with open(file_path,'w') as f:
        f.write(data_value)

if __name__ == '__main__':
    data = {
        "app":{
        "aaaa":"bbbbb"
        }
    }
    write_value()

# DataPath = handle_ini.get_Inivalue('result','mock')
# print(DataPath)
# print(get_Jsonvalue(DataPath,'api3/getbanneradvertver2'))
