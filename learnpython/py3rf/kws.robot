*** Keywords ***
testMyKey
        [Arguments]  ${par1}  ${par2}
        log  ${par1}
        log  ${par2}

click_element_wait
        [Arguments]  ${locator}
        [Documentation]   点击元素
        wait until element is visible  ${locator}  10
        click element  ${locator}

input_text_wait
         [Arguments]  ${locator}  ${value}
         [Documentation]   输入值
         wait until element is visible  ${locator}  10
         input text  ${locator}  ${value}