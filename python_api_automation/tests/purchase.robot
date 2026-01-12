*** Settings ***
Library    ../libraries/DotEnv.py
Resource    ../resources/keywords.robot

*** Test Cases ***
Successful Purchase With Minimal Fields
    ${response}=    Create Purchase Request
    Status Should Be    201    ${response}
    Dictionary Should Contain Value
    ...    ${response.json()}    SUCCEEDED
