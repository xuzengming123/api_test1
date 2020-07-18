import pprint
from base.runMethod import BaseRequest
import requests
import json
import unittest
url = 'https://www.imooc.com/apiw/logo'
data = {
    'v':'5.1.2',
    'v_code':'5120',
    'token':'5c1d2b3f9ac501dc8a5c2345bd7b9603',
    'uuid':'41b650ef846688193728ff7381eb6c1c',
    'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiZTIxNmY0OWMzZGQ2NmQwZTVjNzNiZDE4ZDI2MmJjOTciLCJkZXZpY2UiOiJtb2JpbGUifQ.gm0p9UKTfosbv4buUlD1u5d0-T2EtXNd5QQUe9ZlHe0',
    'app_id':'1',
    'plat_id':'2',
    'timestamp':'1560660339989',
    'uid':'7213561',
    'type':'0'
}
# res_text = requests.get(url,verify=False).text
# res = requests.post(url=url,data=data,verify=False)
# print(res.text)
class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        print('测试开始')
    def test_01(self):
        res_text = BaseRequest.run_main('get',url,data)
        print(res_text)
    def tearDown(self) -> None:
        print('测试结束')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCase01('test_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
# cookiejar = res.cookies
# cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
# print(cookiedict)
