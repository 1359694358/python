import unittest
class MyCalse(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def test_fuck(self):
        print("test fuck")

print(__name__)
if __name__ == '__main__':
    unittest.main()#运行所有的测试用例