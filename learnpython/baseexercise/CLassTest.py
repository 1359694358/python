
class Reflect:
    count=0
    def __init__(self):
        self.count+=1
    def method(self):
        print("call method",self.count)

    proper="proper"


reflect=Reflect()

ff=Reflect()

ff.method()

from pkg.TestPkg import Test
from pkg.TestPkg import callF
tpk=Test()
tpk.fuck()
callF()