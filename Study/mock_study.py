#coding=utf-8
import mock
import requests
import unittest


# url = "http://www.baidu.com"
# data = {
# "username":"111111",
# "password":"11112"
# }
def post_request(url,data):
    res = requests.post(url,data).json()
    return res

def get_request(url,params):
    res = requests.get(url,params).json()
    return res


class TestLogin(unittest.TestCase):
    def setUp(self):
        print('case开始执行')
    def tearDown(self):
        print('case执行结束')
    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username":"111111"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual('11222',res())

if __name__ == '__main__':
    unittest.main()