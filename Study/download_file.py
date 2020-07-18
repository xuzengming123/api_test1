import requests
import json
download_url = 'http://file.mukewang.com/imoocweb/webroot/mobile/imooc7.2.010102001android.apk'
cookie = {
    "apsid":"I5ZTVmZmUzMGE1NDY2OTljZjFjYzkyMTMyMjk3MmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzIxMzU2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNdXNoaXNoaV94dUAxNjMuY29tAAAAAAAAAAAAAAAAADVjZDY5ZWYxMGQ2MmFlZDVmNTJkYWQ0ZWNhNjU5MjZhz%2BMFXc%2FjBV0%3DZW"
}

res = requests.get(download_url)
with open('mukewang.apk','wb') as f:
    f.write(res.content)