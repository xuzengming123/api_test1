# coding=utf-8
import requests
import json


class BaseRequest:
    @classmethod
    def send_post(cls, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, header=header).text
        else:
            res = requests.post(url=url, data=data).text
        return res

    @classmethod
    def send_get(cls, url, data=None, header=None):
        if header is not None and data is not None:
            res = requests.get(url, params=data, header=header).text
        elif header is not None and data is None:
            res = requests.get(url=url, header=header).text
        else:
            res = requests.get(url=url).text
        return res

    @classmethod
    def run_main(cls, method, url, data):
        if method == 'get':
            res = cls.send_get(url, data)
        else:
            res = cls.send_post(url, data)
        try:
            res = json.loads(res)
        except:
            return res
