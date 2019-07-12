import datetime
import json
import time

import requests


dt=int(time.time())
print(str(dt))
url="http://ip.taobao.com/service/getIpInfo.php?ip=myip&time="+str(dt)
print(url)
response=requests.get(url)
print(response.text)
if response.status_code==200:
    jobj=json.loads(response.text)
    print(jobj["data"]["ip"])




mylist=["php","java","kotlin","cpp","erlang"]

for i in range(len(mylist)):
    pass


score=int(input("please input score num:"))
if score>=90:
    print("perfect")
elif score>=80:
    print("well done")
elif score>=60:
    print("so so")
else:
    print("failed")
