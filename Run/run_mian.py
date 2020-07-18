#_*_ coding:utf-8 _*_
import time
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import os,sys
from base.unittest1 import SearchTest
from base.unittest2 import TestMath
from Untill.handle_excel import excel_data
from base.runMethod import BaseRequest
from Untill.handle_ini import handle_ini
class RunMain:
    def run_case(self):
        #获取总行数
        rows = excel_data.get_rows()
        for i in range(rows-1):
            #获取每一行的数据。i是从0开始的，所以要+2，才能从第一行算
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[5]
                url = data[4]
                data1 = data[6]
                BaseRequest.run_main(method,url,data1)


if __name__ == '__main__':
    run = RunMain()
    run.run_case()

























# #获取输出报告的路径
# dirss = os.path.abspath('../Report/')
# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# HtmlFile = os.path.join(dirss,'Testreport' + now + '.html')
#
#
# if __name__ == '__main__':
#
#     #TestLoader().loadTestsFromTestCase得到测试文件中所有测试方法
#     search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
#     test_math = unittest.TestLoader().loadTestsFromTestCase(TestMath)
#     #创建测试套件，集合测试
#     suite = unittest.TestSuite([search_tests,test_math])
#     with open(HtmlFile, "wb") as fp:
#         runner = HTMLTestRunner(stream=fp,title=u'测试报告', description=u'执行情况',verbosity=2)
#         #执行
#         runner.run(suite)
#         fp.close()
#
