from selenium.webdriver.common.by import By

from BaseSelenium import BaseSelenium


class ZhengZhouUnivercity(BaseSelenium):
    def __init__(self):
        BaseSelenium.__init__(self)
        return

zhenzhou=ZhengZhouUnivercity()
zhenzhou.openUrl("http://www.zzu.edu.cn/?tdsourcetag=s_pcqq_aiomsg")

frame=zhenzhou.waitFindElementByValue(By.NAME,"zzu_top_6")
print(frame)
zhenzhou.switch_to_iframe(frame)
zhenzhou.move2Element(By.XPATH,"//li[contains(text(),'院系专业')]")
zhenzhou.clickElement(By.XPATH,"//span[contains(text(),'实验动物中心')]")
zhenzhou.switch_to_default_content()
zhenzhou.openNewTable("https://www.baidu.com")
zhenzhou.switch_table(0)
zhenzhou.switch_to_iframe("zzu_top_6")
zhenzhou.move2Element(By.XPATH,"//li[contains(text(),'院系专业')]")
zhenzhou.clickElement(By.XPATH,'//span[contains(text(),"省医药科学研究院")]/../span[2]')

zhenzhou.forceWait(9)
zhenzhou.quit()