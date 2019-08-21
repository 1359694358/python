*** Keywords ***
testMyKey
        [Arguments]  ${par1}  ${par2}
        log  ${par1}
        log  ${par2}
mouse_over_wait
        [Arguments]  ${locator}
        [Documentation]   点击元素
        wait until element is visible  ${locator}  10
        mouse over  ${locator}

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


select_frame_wait
        [Arguments]  ${locator}
         wait until element is visible  ${locator}  10
         select frame  ${locator}