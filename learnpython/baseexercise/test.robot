*** Settings ***
Library           Selenium2Library

*** Test Cases ***
testcase
     : FOR    ${uname}    ${psw}    ${repsw}    ${email}    IN
    ...    test_001    test_001    test_001    test_001@qq.com
    ...    test_002    test_002    test_002    test_002@qq.com
    ...    test_003    test_003    test_003    test_003@qq.com
    \    Log Many    ${uname}    ${psw}    ${repsw}    ${email}