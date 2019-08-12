import unittest

from dy.selenium.toolkit import SeleniumToolKit
from dy.selenium.yamlhandle import readYml
class SeleniumCase(unittest.TestCase):SeleniumToolKit(brower_cfgpath)
        print(self.cas
    def __init__(self,casepath,brower_cfgpath):
        SeleniumCase.__init__(self,"")
        self.caseconfig=readYml(casepath)
        self.driverkit=econfig)
        return

    def setUp(self):
        # case =SeleniumCase('./testcase.yml','./browser_config.yml')
        pass

    def tearDown(self):
        self.driverkit.quit()
        pass