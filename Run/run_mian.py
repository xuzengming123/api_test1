#_*_ coding:utf-8 _*_
import time
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import os,sys,json
from base.unittest1 import SearchTest
from base.unittest2 import TestMath
from Untill.handle_excel import excel_data
from base.runMethod import BaseRequest
from Untill.handle_ini import handle_ini
from Untill.handle_result import ExpectationResultMoed
# print(handle_ini.get_value('id','case'))
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
                result_moed = data[8]   #预期结果方式
                ExpectationResult = data[9] #预期结果
                res = BaseRequest.run_main(method,url,data1)
                #code:接口返回的code，message：接口返回的message
                code = res['errorCode']
                message = res['errorDesc']
                # print(ExpectationResult)
                if result_moed == 'mec':
                    # config_message: code_message.json文件中的code对应的message
                    # config_message = ExpectationResultMoed.get_message(url,code)
                    #excel_message:从excel中获取code对应的message
                    excel_message = ExpectationResultMoed.get_excel_message(ExpectationResult,url,code)
                    # print('url:',url,'code:',code)
                    # print('接口返回的message--------->',message,'json文件中定义的config_messag---------->e',config_message)
                    # print('接口返回的message--------->', message, 'excel文件中预期结果---------->', excel_message)
                    if message == excel_message:
                        print('case通过')
                    else:
                        print('case失败')
                if result_moed == 'errorcode':
                    if ExpectationResult == code:
                        print('case通过')
                    else:
                        print('case失败')
                if result_moed == 'json':
                    if code == 1000:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    #通过json文件获取预期结果
                    excepect_result = ExpectationResultMoed.get_result_from_json(url,status_str)
                    print(excepect_result)
                    # print(excepect_result)
                    #通过excel文件获取预期结果
                    # excepect_result = ExpectationResultMoed.get_result_from_excel(ExpectationResult,url,status_str)
                    # 开始校验结果
                    # result = ExpectationResultMoed.handle_result_json(res,excepect_result)
                    # print(result)



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
