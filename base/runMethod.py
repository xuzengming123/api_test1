# coding=utf-8
import requests
import json
from Untill.handle_ini import handle_ini
from Untill.handle_json import get_Jsonvalue

class BaseRequest:
    @classmethod
    def send_post(cls, url, data,cookie=None,get_cookie=None,header=None):
        response = requests.post(url=url,data=data,cookies=cookie,headers=header,verify=False)
        res = response.text
        return res

    @classmethod
    def send_get(cls, url,data,cookie=None,get_cookie=None,header=None):
        response = requests.get(url=url,params=data,cookies=cookie,headers=header,verify=False)
        res = response.text
        return res

    @classmethod
    def run_main(cls, method,url,data,cookie=None,get_cookie=None,header=None):

        #这行代码主要是为了模拟返回数据（user_data.json中的数据）
        # DataPath = handle_ini.get_value('user_data', 'mock')
        # return get_value(DataPath,url)
        base_url = handle_ini.get_Inivalue('host','server')
        if 'http' not in url:
            url = base_url + url
        if method == 'get':
            res = cls.send_get(url, data,cookie,get_cookie,header)
        else:
            res = cls.send_post(url, data,cookie,get_cookie,header)
        try:
            res = json.loads(res)
        except:
            return res
        return res

# res = BaseRequest.run_main('post','http://www.imooc.com/api3/getbanneradvertver2','{"username":"111111"}')
# print(res)