*** Settings ***
Library  Selenium2Library


*** Test Cases ***
normalLoopCase
    :FOR    ${item}    IN RANGE     2   10      2
    \   log  ${item}

exitLoopCase
    :FOR    ${item}     IN RANGE    10
    \   ${result}   evaluate   ${item}*10
    \   ${result}   convert to number  ${result}
    \   exit for loop if    ${result}>30
    \   log    ${result}