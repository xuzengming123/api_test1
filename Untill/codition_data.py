# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 9:19
# @Author  : xuzengming
# @FileName: codition_data.py.py
# @Software: PyCharm
from Untill.handle_excel import excel_data
from jsonpath_rw import parse
import json
def split_data(data):
    '''
    拆分单元格数据
    :param data:
    :return:
    '''
    #imooc_005>data:banner:id
    case_id = data.split('>')[0]
    rule_data = data.split('>')[1]
    return case_id,rule_data


def depend_data(data):
    '''
    获取依赖结果集(单元格内容)
    :param data:
    :return:
    '''
    case_id = data.split('>')[0]
    row_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(row_number,14)
    return data

def get_depend_data(res_data,key):
    '''
    获取依赖字段
    :param res_data:请求返回的数据
    :param key:依赖字段的路径
    :return:
    '''
    json_exe = parse(key)
    madle =json_exe.find(res_data)
    for math in madle:
        return math.value

def get_data(data):
    '''
    获取依赖数据
    :param data:
    :return:
    '''
    res_data = depend_data(data)
    rule_data =split_data(data)[1]
    res_data = json.loads(res_data)
    return get_depend_data(res_data,rule_data)



if __name__ == '__main__':
    data = {"status": 1, "data": [], "errorCode": 1006, "errorDesc": "token error", "timestamp": 1595916225257}
    key = 'status'
    # print(get_depend_data(data, key))
    # print(depend_data('imooc_005>stutas'))
    print(get_data('imooc_005>status'))
    # print(get_depend_data(data,key))