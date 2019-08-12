import unittest



class MyTestCase(unittest.TestCase):

        # unittest.TestCase.__init__("test_fuck")#,'./testcase.yml','./browser_config.yml')

    def test_Fun(self):
        print("testFUn")
    def runTest(self):
        # self.driverkit.openUrl("https://www.baidu.com")
        # self.driverkit.forceWait(3)
        print("test fuck")
        # str1="aaa"
        # str2="AAA"
        # print(bool(re.search(str1,str2,re.IGNORECASE)))
        # print(chr(75))
        # print(ord('A'))
def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase())
    return suite
if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main(defaultTest = 'suite')#运行所有的测试用例