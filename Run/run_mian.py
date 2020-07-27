#_*_ coding:utf-8 _*_
import time
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import os,sys,json
from base.unittest1 import SearchTest
from base.unittest2 import TestMath
from Untill.handle_excel import excel_data
from base.runMethod import BaseRequest
from Untill.handle_ini import handle_init
from Untill.handle_result import ExpectationResultMoed
from Untill.handle_excel import excel_data
from Untill.handle_cookie import get_cookie_value,write_cookie
from Untill.handle_header import get_header
from Untill.codition_data import get_data
# print(handle_ini.get_value('id','case'))
class RunMain(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_run_case(self):
        #获取总行数
        rows = excel_data.get_rows()

        for i in range(rows-1):
            cookie = None  # 初始化cookie为None
            get_cookie = None
            header=None
            #获取每一行的数据。i是从0开始的，所以要+2，才能从第一行算
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[6]
                is_depeng = data[3]
                data1 = json.loads(data[7])
                if is_depeng:
                    '''获取依赖数据'''
                    depend_key = data[4]
                    depend_data = get_data(is_depeng)
                    data1[depend_key] = depend_data
                url = data[5]
                cookie_method = data[8]    #cookie操作方式
                is_header = data[9]
                result_moed = data[10]   #预期结果方式
                ExpectationResult = data[11] #预期结果
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie = {"is_cookie":"web"}
                if is_header == 'yes':
                    header = get_header()
                res = BaseRequest.run_main(method,url,data1,cookie,get_cookie,header)
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
                        excel_data.excel_wirte_data(i+2,13,'通过')
                    else:
                        excel_data.excel_wirte_data(i+2,13,'失败')
                if result_moed == 'errorcode':
                    if ExpectationResult == code:
                        excel_data.excel_wirte_data(i+2,13,'通过')
                    else:
                        excel_data.excel_wirte_data(i+2,13,'失败')
                if result_moed == 'json':
                    if code == 1000:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    #通过json文件获取预期结果
                    # excepect_result = ExpectationResultMoed.get_result_from_json(url,status_str)
                    # print(excepect_result)
                    # print(excepect_result)
                    #通过excel文件获取预期结果
                    excepect_result = ExpectationResultMoed.get_result_from_excel(ExpectationResult,url,status_str)
                    # 开始校验结果
                    result = ExpectationResultMoed.handle_result_json(excepect_result,res)
                    if result:
                        excel_data.excel_wirte_data(i+2,13,'通过')
                    else:
                        excel_data.excel_wirte_data(i+2,13,'失败')
                        excel_data.excel_wirte_data(i+2,14,json.dumps(res))



# if __name__ == '__main__':
#     run = RunMain()
#     run.run_case()

# #获取输出报告的路径
dirss = os.path.abspath('../Report/')
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = os.path.join(dirss,'Testreport' + now + '.html')

#
if __name__ == '__main__':

    #TestLoader().loadTestsFromTestCase得到测试文件中所有测试方法
    run_main_tests = unittest.TestLoader().loadTestsFromTestCase(RunMain)
    # test_math = unittest.TestLoader().loadTestsFromTestCase(TestMath)
    #创建测试套件，集合测试
    suite = unittest.TestSuite([run_main_tests])
    with open(HtmlFile, "wb") as fp:
        runner = HTMLTestRunner(stream=fp,title=u'测试报告', description=u'执行情况',verbosity=2)
        #执行
        runner.run(suite)
        fp.close()

