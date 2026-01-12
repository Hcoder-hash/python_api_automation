*** Settings ***
Library    Collections
Library    OperatingSystem
Library    uuid
Library    ../libraries/DotEnv.py

*** Keywords ***
Create Auth Headers
    ${idempotency}=    Evaluate    str(__import__('uuid').uuid4())
    &{headers}=    Create Dictionary
    ...    public-api-key=${PUBLIC_API_KEY}
    ...    private-secret-key=${PRIVATE_SECRET_KEY}
    ...    x-idempotency-key=${idempotency}
    ...    Content-Type=application/json
    RETURN    ${headers}
