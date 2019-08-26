*** Settings ***
Library  Selenium2Library
Resource   variable.robot
Resource   kws.robot
Resource   ./login/login.robot
#Suite Setup  #所有用例执行之前
#Suite Teardown  #所有用例执行后
Test Setup  open_chrome  ${zhendaurl}
Test Teardown  close_browser

*** Test Cases ***
case1
       ${anodecount}    get matching xpath count   //a
       should be equal   ${anodecount}   52
       log  ${anodecount}
       xpath should match x times   //a  52
       select_frame_wait   name=zzu_top_6
       mouse_over_wait   xpath=//li[contains(text(),'院系专业')]
       click_element_wait   xpath=//span[contains(text(),'实验动物中心')]
       ${windows}   get window handles
       ${index}  evaluate  ${windows}[0]
       sleep  3s
       select window   ${index}
       sleep  3s