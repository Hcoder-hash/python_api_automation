*** Settings ***
Library    ../libraries/DotEnv.py
Resource    ../resources/keywords.robot

*** Test Cases ***
Purchase With Invalid Card
    ${headers}=    Create Auth Headers
    &{card}=    Create Dictionary
    ...    number=4242424242424241
    ...    expiration_month=12
    ...    expiration_year=30
    ...    security_code=123

    &{payment_method}=    Create Dictionary
    ...    type=CARD
    ...    card=${card}

    &{payload}=    Create Dictionary
    ...    amount=1000
    ...    currency=USD
    ...    workflow=DIRECT
    ...    payment_method=${payment_method}

    Create Session    yuno    ${BASE_URL}
    ${response}=    POST On Session
    ...    yuno
    ...    /payments
    ...    json=${payload}
    ...    headers=${headers}

    Status Should Be    400    ${response}
