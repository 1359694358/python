*** Settings ***
Library     Selenium2Library
Resource   variable.robot
Resource   kws.robot
Resource   ./login/login.robot
#Suite Setup  #所有用例执行之前
#Suite Teardown  #所有用例执行后
Test Setup  open_browser  ${url}  chrome
Test Teardown  close_browser
Library  rfinvoke.py  #导入自定义py文件 用全名
*** Test Cases ***
cassName01
   log   测试输出
   sendEmail  1  2
   testMyKey  testkp1  testkp2
   click_element_wait  ${loginbtn}
   input_text_wait  xpath=/html/body/form/p[1]/input  ${uname}
   input_text_wait  xpath=/html/body/form/p[2]/input  ${psw}
   click_element_wait  xpath=/html/body/form/p[3]/button
   element text should be  xpath=//p[contains(text(),"welcome")]  welcome${uname}
   sleep  3s
