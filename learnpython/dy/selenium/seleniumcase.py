import unittest

from dy.selenium.toolkit import SeleniumToolKit
from dy.selenium.yamlhandle import readYml
class SeleniumCase(unittest.TestCase,SeleniumToolKit):
    def __init__(self,casepath,brower_cfgpath):
        unittest.TestCase.__init__(self,"")
        SeleniumToolKit.__init__(self,brower_cfgpath)
        self.caseconfig=readYml(casepath)
        print(self.caseconfig)
        return

    def setUp(self):
        # case =SeleniumCase('./testcase.yml','./browser_config.yml')
        pass

    def tearDown(self):
        self.quit()
        pass