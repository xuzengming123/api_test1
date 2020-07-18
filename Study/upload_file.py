
#request上传文件操作

import requests
import json

url = 'https://www.imooc.com/user/postpic'
# file = {
#     "fileField":("文件名称",open('文件路径','rb'),'文件类型')
# }
file = {
    "fileField":("1.png",open(r'C:\Users\29276\Desktop\1.png','rb'),'image/png'),
    'type':'1'
}
cookie = {
    "apsid":"I5ZTVmZmUzMGE1NDY2OTljZjFjYzkyMTMyMjk3MmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzIxMzU2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNdXNoaXNoaV94dUAxNjMuY29tAAAAAAAAAAAAAAAAADVjZDY5ZWYxMGQ2MmFlZDVmNTJkYWQ0ZWNhNjU5MjZhz"
}
res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)

