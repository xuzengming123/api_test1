# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 16:43
# @Author  : xuzengming
# @FileName: handle_result.py.py
# @Software: PyCharm

import sys, os, json
from Untill.handle_json import get_Jsonvalue
from Untill.handle_ini import handle_ini


# print(get_Jsonvalue(r'E:\api_test3_owner\Config\user_data.json','api3/beta4'))

class ExpectationResultMoed:
    @classmethod
    def get_message(cls, key, code):
        '''
        获取code对应的message信息
        :param key: 接口名
        :param code: code值
        :return:
        '''
        DataPath = handle_ini.get_Inivalue('code_message', 'mock')
        data = get_Jsonvalue(DataPath, key)
        if data is not None:
            for i in data:
                message = i.get(str(code))
                if message:
                    return message
        return None


if __name__ == '__main__':
    print(ExpectationResultMoed.get_message('api3/getbanneradvertver2', '1008'))
