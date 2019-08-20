*** Variables ***
${url}  http://127.0.0.1:5000/
${uname}  15902127953
${psw}  123456
*** Settings ***
Library           Selenium2Library

#Suite Setup  #所有用例执行之前
#Suite Teardown  #所有用例执行后
Test Setup  open_browser  ${url}  chrome
Test Teardown  close_browser
Library  rfinvoke.py  #导入自定义py文件 用全名
*** Test Cases ***
cassName01
   log   测试输出
   sendEmail  1  2
   click element  xpath=/html/body/a
   input text  xpath=/html/body/form/p[1]/input  ${uname}
   input text  xpath=/html/body/form/p[2]/input  ${psw}
   click element  xpath=/html/body/form/p[3]/button
   element text should be  xpath=//p[contains(text(),"welcome")]  welcome${uname}
   sleep  3s