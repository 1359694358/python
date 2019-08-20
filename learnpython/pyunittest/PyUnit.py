# from dy.testrunner.HTMLTestRunner import HTMLTestRunner
import time
import unittest

class CustomCs1(unittest.TestCase):
    def test1(self):
        print("CustomCs1 test1")
        pass

    def test2(self):
        print("CustomCs1 test2")
        pass

class CustomCs2(unittest.TestCase):
    def testa(self):
        print("CustomCs2 testa")
        pass

    def testA(self):
        print("CustomCs2 testA")
        pass
    def hello(self):
        print('hello')

#first way   mouse click the pycharm testcase class  or test method  and run

#second way
if __name__ == '__main__':
    print("<---------test suite direct add test case run method")
    testsuite=unittest.TestSuite()
    testsuite.addTest(CustomCs1("test2"))
    testsuite.addTest(CustomCs1("test1"))
    testsuite.addTests([CustomCs2("testa")])
    unittest.TextTestRunner().run(testsuite)
    print("test suite direct add test case run method---------/>")

if __name__ == '__main__':
    print("<---------test suite  use TestLoader add test case")
    testsuite=unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(CustomCs1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromName('pyunittest.PyUnit.CustomCs2'))
    unittest.TextTestRunner().run(testsuite)
    print("test suite  use TestLoader add test case--------->")