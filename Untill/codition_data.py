# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 9:19
# @Author  : xuzengming
# @FileName: codition_data.py.py
# @Software: PyCharm
from Untill.handle_excel import excel_data
from jsonpath_rw import parse
def split_data(data):
    '''
    拆分单元格数据
    :param data:
    :return:
    '''
    #imooc_005>data:banner:id
    case_id = data.split('>')[0]
    rule_data = data.split('>')[1]
    return case_id,rule_data


def depend_data(data):
    '''
    获取依赖结果集(单元格内容)
    :param data:
    :return:
    '''
    case_id = data.split('>')[0]
    row_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(row_number,13)
    return data

def get_depend_data(res_data,key):
    '''
    获取依赖字段
    :param res_data:请求返回的数据
    :param key:依赖字段的路径
    :return:
    '''
    json_exe = parse(key)
    madle =json_exe.find(res_data)
    for math in madle:
        return math.value

def get_data(data):
    '''
    获取依赖数据
    :param data:
    :return:
    '''
    res_data = depend_data(data)
    rule_data =split_data(data)[1]
    return get_depend_data(res_data,rule_data)


if __name__ == '__main__':
    data = {"status":0,"data":{"banner":[{"id":2262,"type":6,"type_id":330,"name":"\u524d\u7aef\u4e0b\u4e00\u4ee3\u5f00\u53d1\u8bed\u8a00TypeScript  \u4ece\u57fa\u7840\u5230axios\u5b9e\u6218","pic":"http:\/\/szimg.mukewang.com\/5cf721df09fc2be500000000.jpg","links":""},{"id":1648,"type":6,"type_id":169,"name":"Python3\u5165\u95e8\u673a\u5668\u5b66\u4e60 \u7ecf\u5178\u7b97\u6cd5\u4e0e\u5e94\u7528","pic":"http:\/\/szimg.mukewang.com\/5d0ed2d9085bd6ed09000300.jpg","links":""},{"id":1875,"type":6,"type_id":316,"name":"\u4ece\u57fa\u7840\u5230\u5b9e\u6218 \u624b\u628a\u624b\u5e26\u4f60\u638c\u63e1\u65b0\u7248Webpack4.0","pic":"http:\/\/szimg.mukewang.com\/5d0ed2ca086a9e6f09000300.jpg","links":""},{"id":1999,"type":6,"type_id":342,"name":"\u7eaf\u6b63\u5546\u4e1a\u7ea7\u5e94\u7528 Node.js Koa2\u5f00\u53d1\u5fae\u4fe1\u5c0f\u7a0b\u5e8f\u670d\u52a1\u7aef","pic":"http:\/\/szimg.mukewang.com\/5ceb5d370955f30f09000300.jpg","links":""},{"id":2158,"type":99,"type_id":0,"name":"Spring Cloud\u5fae\u670d\u52a1\u5f00\u53d1\u5b9e\u8df5","pic":"http:\/\/img2.mukewang.com\/5d088c4009bbebc009000300.jpg","links":"https:\/\/www.imooc.com\/read\/37"},{"id":1709,"type":6,"type_id":354,"name":"Node.js\u5f00\u53d1\u4eff\u77e5\u4e4e\u670d\u52a1\u7aef \u6df1\u5165\u7406\u89e3RESTful API","pic":"http:\/\/szimg.mukewang.com\/5d0ed27508f7d96909000300.jpg","links":""}],"pic":[{"pic":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/actual_day@3x.png","pic_night":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/actual_night@3x.png","type":2},{"pic":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/path_day@3x.png","pic_night":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/path_night@3x.png","type":6},{"pic":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/question_day@3x.png","pic_night":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/question_night@3x.png","type":3},{"pic":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/note_day@3x.png","pic_night":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/note_night@3x.png","type":4},{"pic":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/discover_day@3x.png","pic_night":"http:\/\/www.imooc.com\/static\/img\/andriod\/pic\/discover_night@3x.png","type":5}]},"errorCode":1001,"errorDesc":"\u6210\u529f","timestamp":1561269343507}
    key = 'data.banner.[0].id'
    print(get_depend_data(data,key))