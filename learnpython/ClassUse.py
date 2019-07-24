
class Human:
    pbPro=1#类变量
    _privateVar=1
    pubVar=2
    def __init__(self,age,sex):
        self.age=age#实例变量
        self.sex=sex

    def _privateMthod(self):
        print("private method:",self._privateVar)

    def printInfo(self):
        print("age:{},sex:{}".format(self.age,self.sex))
human=Human(30,1)
Human.pbPro=2
print(human.pbPro)
human.pbPro=3
print(human.pbPro)
human.fuck=11
print(human.age)
human.printInfo()
print(human.fuck)
