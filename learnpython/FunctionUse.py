

def fuck():
    """
    :param par: object param
    :return: return void
    """
    print("fuck")

def fuck(boy,gril):
    print(boy+gril)


fuck("FF","1222")

'''
 variable args
'''

def say(*args):
    for item in args:
        print(item)


say(1,2,3)

def keyWordArg(name,age,**kwargs):
    print(name,age,kwargs)
    pass

keyWordArg("ming",30,time=30,f="fuck")

def keyWordArg2(**kwargs):
    print(kwargs)

keyWordArg2(name="11",age=20)

def  noneFun(name=None):
    print(name)

noneFun()

listL=[]
listL.insert(1,12)

print(listL)


def  papapa(a,b,c=3,*args,**kwargs):
    pass


"""
  lamada  express  only one express
"""

f=lambda arg1,arg2:arg1+arg2
result=f(1,2)
print(result)

xxoo=lambda boy,*girl,**tools:print(boy+" fuck "+str(girl)+str(tools))

xxoo("Jay","Senina","Ella","YangMi","WangO",shoes="siwa")


def jiechen(num):
    if num==1:
        return num
    return num*(jiechen(num-1))

num=input("please input a integer:")
print(jiechen(int(num)))