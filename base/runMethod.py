# coding=utf-8
import requests
import json
from Untill.handle_ini import handle_init
from Untill.handle_json import get_Jsonvalue
from Untill.handle_cookie import write_cookie

class BaseRequest:
    @classmethod
    def send_post(cls, url, data,cookie=None,get_cookie=None,header=None):
        response = requests.post(url=url, data=data, cookies=cookie,headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res

    @classmethod
    def send_get(cls, url,data,cookie=None,get_cookie=None,header=None):
        response = requests.get(url=url,params=data,cookies=cookie,headers=header,verify=False)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res

    @classmethod
    def run_main(cls, method,url,data,cookie=None,get_cookie=None,header=None):

        #这行代码主要是为了模拟返回数据（user_data.json中的数据,但是不会被抓包抓到）
        # DataPath = handle_init.get_Inivalue('user_data', 'mock')
        # return get_Jsonvalue(DataPath,url)
        base_url = handle_init.get_Inivalue('host','server')
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

# res = BaseRequest.run_main('post','http://www.imooc.com/api3/getbanneradvertver2','{"username":"111111"}',get_cookie={"is_cookie":"web"})
# print(res)