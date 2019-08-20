from dy.selenium.seleniumcase import  SeleniumCase
import pyunittest
class ReadConfigRunCase(SeleniumCase):
    def __init__(self):
        SeleniumCase.__init__(self,'./testcase.yml','./browser_config.yml')
        pass

if __name__=='main':
    pyunittest.main()
