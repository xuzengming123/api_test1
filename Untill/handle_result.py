# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 16:43
# @Author  : xuzengming
# @FileName: handle_result.py.py
# @Software: PyCharm

import sys, os, json
from Untill.handle_json import get_Jsonvalue
from Untill.handle_ini import handle_init
from Untill.handle_excel import excel_data
from deepdiff import DeepDiff
from Untill.handle_json import get_Jsonvalue


# print(get_Jsonvalue(r'E:\api_test3_owner\Config\user_data.json','api3/beta4'))

class ExpectationResultMoed:
    @classmethod
    def get_message(cls, key, code):
        '''
        获取json文件的code对应的message信息
        :param key: 接口名
        :param code: code值
        :return:
        '''
        DataPath = handle_init.get_Inivalue('code_message', 'mock')
        data = get_Jsonvalue(DataPath, key)
        if data is not None:
            for i in data:
                message = i.get(str(code))
                if message:
                    return message
        return None

    @classmethod
    def get_excel_message(cls,message_data,key,code):
        '''
        从excel中获取code对应的message信息
        :param key: 接口名
        :param code: code值
        :return:
        '''
        message_data = json.loads(message_data)
        message_list = message_data.get(key)
        if message_list != None:
            for i in message_list:
                mes = i.get(str(code))
                if mes:
                    return mes
        return None

    @classmethod
    def handle_result_json(cls,d1,d2):
        '''
        校验格式,对比d1,d2两个对象。可以相等则返回True，否则返回Flase
        :return:
        '''
        if isinstance(d1,dict) and isinstance(d2,dict):
            cmp_dict = DeepDiff(d1,d2,ignore_order=True).to_dict()
            if cmp_dict.get('dictionary_item_added'):
                return False
            else:
                return True
        return False

    @classmethod
    def get_result_from_json(cls,url,status):
        '''
        从json文件中获取接口返回的数据（预期结果。）
        :param url: 接口名
        :param status: 接口状态
        :return:
        '''
        DataPath = handle_init.get_Inivalue('result','mock')
        ResultData = get_Jsonvalue(DataPath,url)

        if ResultData != None:
            for i in ResultData:
                message = i.get(status)
                if message:
                    return message
        else:
            return None


    @classmethod
    def get_result_from_excel(cls,messageData,url,status):
        '''
        从excel中获取预期结果。
        :param messageData: 接口数据
        :param url: 接口名
        :param status: 返回的状态
        :return:
        '''
        message_data = json.loads(messageData)
        if messageData:
            message_list = message_data.get(url)
            if message_list != None:
                for i in message_list:
                    mes = i.get(status)
                    if mes:
                        return mes
            return None
        return '该单元格没有数据'



if __name__ == '__main__':
    # print(ExpectationResultMoed.get_result_from_json('api3/getdownrecommend','error'))
    data = excel_data.get_cell_value(2,10)
    print(data)
    print(ExpectationResultMoed.get_result_from_excel(data,'api3/getbanneradvertver2','error'))
#     a = {"api3/getdownrecommend":[
#     {
#     "sucess":
#         {
#             "status":0,
#             "data":{
#                 "banner":[
#                     {
#                         "id":1709,
#                         "type":6,
#                         "type_id":354,
#                         "name":"Node.js开发仿知乎服务端 深入理解RESTful API",
#                         "pic":"http://szimg.mukewang.com/5d0ed27508f7d96909000300.jpg",
#                         "links":""
#                     }
#                 ],
#                 "pic":[
#                     {
#                         "pic":"http://www.imooc.com/static/img/andriod/pic/discover_day@3x.png",
#                         "pic_night":"http://www.imooc.com/static/img/andriod/pic/discover_night@3x.png",
#                         "type":5
#                     }
#                 ]
#             },
#             "errorCode":1000,
#             "errorDesc":"成功",
#             "timestamp":0
#         }
#     },
#     {
#     "error":{
#         "status":0,
#         "data":"",
#         "errorCode":1002,
#         "errorDesc":"失败",
#         "timestamp":0
#         }
#     }
# ]}
#     b = {"status": 1, "data": [], "errorCode": 1006, "errorDesc": "token error", "timestamp": 1595238866642}
#     print(type(a))
#     print(type(b))
#     print(ExpectationResultMoed.handle_result_json(a,b))