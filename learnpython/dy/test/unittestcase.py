import types
import unittest
'''

class MyTestCase(unittest.TestCase):

        # unittest.TestCase.__init__("test_fuck")#,'./testcase.yml','./browser_config.yml')
    def __init__(self,methodName):
        print(id(self))
        unittest.TestCase.__init__(self,"runTest")
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        return
    def test_Fun(self):
        print("test_Fun")

    def testMM(self):
        print("test_Fun")
    def runTest(self):
        # self.driverkit.openUrl("https://www.baidu.com")
        # self.driverkit.forceWait(3)
        print("test fuck")
        # str1="aaa"
        # str2="AAA"
        # print(bool(re.search(str1,str2,re.IGNORECASE)))
        # print(chr(75))
        # print(ord('A'))'''
import unittest
# 执行测试的类
class WidgetTestCase(unittest.TestCase):

    def tearDown(self):
        self.widget = None

    def testSize(self):
        print(id(self))
        print("testSize")
# 构造测试集
def suite():
    case =WidgetTestCase("testMyMethod")
    print(id(case))
    testMyMethod=lambda self:print("hehe dynamic test method")
    case.testMyMethod=testMyMethod
    setattr(case,"testMyMethod",testMyMethod)
    suite = unittest.TestSuite()
    suite.addTest(case)
    return suite
# 测试
# if __name__ == "__main__":
#     print(1111)
#     unittest.main(defaultTest='suite')
    # suite = unittest.TestSuite()
    # case = WidgetTestCase("testMyMethod")
    # case.testMyMethod=lambda self:print("hehe dynamic test method")
    # case.testMyMethod()
    # suite.addTest(case)
    # suite.addTest(WidgetTestCase("testMyMethod"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # unittest.main(defaultTest = 'suite')
    # unittest.main(defaultTest = 'suite')#运行所有的测试用例

if __name__ == "__main__":
    # unittest.main(defaultTest='suite')
    unittest.mai