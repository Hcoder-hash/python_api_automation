*** Settings ***
Library    RequestsLibrary
Library    FakerLibrary
Library    BuiltIn
Library    ../libraries/DotEnv.py
Resource   auth.resource
Resource   variables.robot

*** Keywords ***
Create Purchase Payload Minimal
    &{card}=    Create Dictionary
    ...    number=4242424242424242
    ...    expiration_month=12
    ...    expiration_year=30
    ...    security_code=123

    &{payment_method}=    Create Dictionary
    ...    type=CARD
    ...    card=${card}

    &{payload}=    Create Dictionary
    ...    amount=${AMOUNT}
    ...    currency=${CURRENCY}
    ...    workflow=${WORKFLOW}
    ...    payment_method=${payment_method}

    RETURN    ${payload}

Create Purchase Request
    ${headers}=    Create Auth Headers
    ${payload}=    Create Purchase Payload Minimal
    Create Session    yuno    ${BASE_URL}
    ${response}=    POST On Session
    ...    yuno
    ...    /payments
    ...    json=${payload}
    ...    headers=${headers}
    RETURN    ${response}
