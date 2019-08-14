#使用from import，从模块里面导入某个方法
from datetime import datetime
from time import * #通配符，导入模块里面所有的变量方法等等
print(datetime.now())#现在的时间
print(time())#时间戳
print('------')


#使用import,直接导入这个模块
import datetime
import time
print(datetime.datetime.now())
print(time.time())