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




mylist=["php","where","fuckyou","cpp","erlang"]

for i in range(len(mylist)):
    itemLen=len(mylist[i])
    if itemLen%2!=0:
        middle=itemLen//2
        itemChar=mylist[i][:middle]+mylist[i][middle:middle+1].upper()+mylist[i][middle+1:]
        mylist[i]=itemChar
print(mylist)
mylist=["php","where","fuckyou","cpp","erlang"]
for item in mylist:
    itemLen = len(item)
    if itemLen%2!=0:
        currentIndex=mylist.index(item)
        middle=itemLen//2
        itemChar=item[:middle]+item[middle:middle+1].upper()+item[middle+1:]
        mylist[currentIndex] = itemChar
print(mylist)


score=int(input("please input score num:"))
if score>=90:
    print("perfect")
elif score>=80:
    print("well done")
elif score>=60:
    print("so so")
else:
    print("failed")
