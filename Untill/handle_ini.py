#coding=utf-8

import os
import configparser
CasePath = os.path.abspath('../Config/')

class HandleInit:
    def load_ini(self):
        '''
        加载
        :return:
        '''
        filePath = CasePath +r'\server.ini'
        conf = configparser.ConfigParser()
        conf.read(filePath,encoding='utf-8')
        return conf

    def get_value(self,key,node=None):
        '''
        获取ini文件的value
        :param key:key
        :param node:节点
        :return:
        '''
        if node is None:
            node = 'server'
        conf = self.load_ini()
        try:
            data = conf.get(node,key)
        except Exception as e:
            print('没有获取到值')
            data = None
        return data

handle_ini = HandleInit()


if __name__ == '__main__':
    handle_ini = HandleInit()
    print(handle_ini.get_value('host', 'xzm'))