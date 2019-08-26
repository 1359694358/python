*** Settings ***
Library  Selenium2Library
Resource   ../variable.robot
Resource   ../kws.robot
Resource   ./login.robot
#Suite Setup  #所有用例执行之前
#Suite Teardown  #所有用例执行后
Test Setup  open_chrome  ${kuaidi100}
Test Teardown  close_browser
#
#*** Test Cases ***
#caseKuaiDi100

*** Keywords ***
open_kuaidi100
    click_element_wait  xpath=//*[@id="welcome"]/a[2]
    input_text_wait  xpath=//*[@id="name"]  13252061368
    input_text_wait  xpath=//*[@id="password"]    123456a
    click_element_wait  xpath=//*[@id="submit"]

query_kuaidi
    [Arguments]  ${numer}
    click_element_wait  xpath=//*[@id="menu-track"]
    sleep  3s
    execute javascript  console.log(${numer})
    input_text_wait  xpath=//input[@id="postid"]     ${numer}
    click_element_wait  xpath=//*[@id="query"]
    mouse_over_wait  xpath=//*[@id="userName"]
    click_element_wait  xpath=//*[@id="userUrl"]/a
    ${windows}   get window handles
    ${index}  evaluate  ${windows}[1]
    select window   ${index}
case_assert
    [Arguments]  ${numer}
     sleep  3s
    page should contain element    xpath=//a[@title='${numer}']


*** Variables ***
${kuaidi_number}    804623382935349595
*** Test Cases ***
kuaidi_gogogo
    open_kuaidi100
    query_kuaidi    ${kuaidi_number}
    case_assert    ${kuaidi_number}