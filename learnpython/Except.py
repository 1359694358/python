try:
    if 1+1>3:
        f=open("test.txt",'r')
except Exception as e:
    print(e)
else:
    print("run else condition")
finally:
    print("excute finnally"*3)


'''custom exception'''

class MyException(Exception):
    def __init__(self,msg):
        pass

def fuck(par):
    if par is None:
        raise MyException("par is null")

try:
    fuck(None)
except Exception as e:
    print(e)


def div(num):
    try:
        num/0
    except Exception as e:
        raise  e

div(3)