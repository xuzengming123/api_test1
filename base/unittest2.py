import unittest
from base.mathtest import *

class TestMath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('执行测试用例')

    def test_add(self):
        print('add')
        self.assertEqual(2,add(2,2),msg='测试失败')
    def test_minus(self):
        print('minus')
        self.assertEqual(4,minus(5,1))
    def test_multi(self):
        self.assertTrue(multi(1,3)==3,msg='计算出错')
    @classmethod
    def tearDownClass(cls):
        print('结束测试')

if __name__ == '__main__':
    unittest.main(verbosity=2)
