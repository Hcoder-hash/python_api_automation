"""
Payment-related step definitions
"""
from behave import when, then
import json
from core.request_builder import RequestBuilder
from core.response_validator import ResponseValidator


@when('I create a purchase request with valid card details')
def step_create_purchase_with_valid_card(context):
    """Create a purchase request with valid card"""
    request_builder = RequestBuilder()
    payload = request_builder.build_purchase_request(
        amount=10000,
        currency="USD",
        card_number="4532015112830366",
        cvv="123",
        expiry="12/25"
    )
    context.request_payload = payload
    context.response = context.manager.post(
        f"{context.api_url}/payments/purchase",
        json=payload
    )


@when('the request contains the required payment information')
def step_verify_request_contains_required_info(context):
    """Verify request has all required payment fields"""
    required_fields = ['amount', 'currency', 'card_number', 'cvv', 'expiry']
    for field in required_fields:
        assert field in context.request_payload, f"Missing required field: {field}"


@then('the purchase should be processed successfully')
def step_purchase_successful(context):
    """Verify purchase was successful"""
    assert context.response.status_code == 200, \
        f"Purchase failed with status code {context.response.status_code}"


@then('the response should contain a valid transaction ID')
def step_verify_transaction_id(context):
    """Verify response contains transaction ID"""
    response_data = context.response.json()
    assert 'transaction_id' in response_data, "Transaction ID not found in response"
    assert response_data['transaction_id'], "Transaction ID is empty"
    context.transaction_id = response_data['transaction_id']


@then('the payment status should be {status}')
def step_verify_payment_status(context, status):
    """Verify payment status"""
    response_data = context.response.json()
    assert 'status' in response_data, "Status not found in response"
    assert response_data['status'] == status, \
        f"Expected status {status}, got {response_data['status']}"


@when('I create a purchase request without required fields')
def step_create_purchase_without_required_fields(context):
    """Create a purchase request with missing fields"""
    payload = {
        "amount": 10000
    }
    context.response = context.manager.post(
        f"{context.api_url}/payments/purchase",
        json=payload
    )


@then('the API should return a validation error')
def step_verify_validation_error(context):
    """Verify API returned validation error"""
    assert context.response.status_code >= 400, "Expected error status code"


@then('the error message should indicate missing fields')
def step_verify_missing_fields_error(context):
    """Verify error message indicates missing fields"""
    response_data = context.response.json()
    assert 'error' in response_data or 'message' in response_data, \
        "Error information not found"


@when('I create a purchase request with amount of {amount:d}')
def step_create_purchase_with_invalid_amount(context, amount):
    """Create a purchase with invalid amount"""
    request_builder = RequestBuilder()
    payload = request_builder.build_purchase_request(
        amount=amount,
        currency="USD",
        card_number="4532015112830366",
        cvv="123",
        expiry="12/25"
    )
    context.response = context.manager.post(
        f"{context.api_url}/payments/purchase",
        json=payload
    )


@then('the API should reject the request')
def step_api_rejects_request(context):
    """Verify API rejected the request"""
    assert context.response.status_code >= 400, "Request should have been rejected"


@then('the response should contain validation error message')
def step_verify_validation_error_message(context):
    """Verify response contains validation error"""
    response_data = context.response.json()
    assert 'error' in response_data or 'message' in response_data, \
        "Validation error not found in response"


@when('I authorize a payment with valid card details')
def step_authorize_payment_valid_card(context):
    """Authorize payment with valid card"""
    request_builder = RequestBuilder()
    payload = request_builder.build_authorization_request(
        amount=10000,
        currency="USD",
        card_number="4532015112830366",
        cvv="123",
        expiry="12/25"
    )
    context.request_payload = payload
    context.response = context.manager.post(
        f"{context.api_url}/payments/authorize",
        json=payload
    )


@when('the authorization request is valid')
def step_verify_authorization_request_valid(context):
    """Verify authorization request is valid"""
    assert 'amount' in context.request_payload
    assert 'card_number' in context.request_payload


@then('the authorization should be successful')
def step_authorization_successful(context):
    """Verify authorization was successful"""
    assert context.response.status_code == 200


@then('the response should contain an authorization code')
def step_verify_auth_code(context):
    """Verify response contains authorization code"""
    response_data = context.response.json()
    assert 'auth_code' in response_data or 'authorization_code' in response_data


@then('the payment status should be AUTHORIZED')
def step_verify_authorized_status(context):
    """Verify payment status is AUTHORIZED"""
    response_data = context.response.json()
    assert response_data.get('status') == 'AUTHORIZED'


@when('I authorize a payment with insufficient funds card')
def step_authorize_insufficient_funds(context):
    """Authorize with insufficient funds card"""
    request_builder = RequestBuilder()
    payload = request_builder.build_authorization_request(
        amount=999999999,
        currency="USD",
        card_number="4000000000000002",
        cvv="123",
        expiry="12/25"
    )
    context.response = context.manager.post(
        f"{context.api_url}/payments/authorize",
        json=payload
    )


@then('the authorization should fail')
def step_authorization_failed(context):
    """Verify authorization failed"""
    assert context.response.status_code >= 400


@then('the response should indicate insufficient funds')
def step_verify_insufficient_funds_error(context):
    """Verify error indicates insufficient funds"""
    response_data = context.response.json()
    error_msg = str(response_data).lower()
    assert 'insufficient' in error_msg or 'funds' in error_msg


@when('I authorize a payment with expired card')
def step_authorize_expired_card(context):
    """Authorize with expired card"""
    request_builder = RequestBuilder()
    payload = request_builder.build_authorization_request(
        amount=10000,
        currency="USD",
        card_number="4000000000000069",
        cvv="123",
        expiry="01/20"
    )
    context.response = context.manager.post(
        f"{context.api_url}/payments/authorize",
        json=payload
    )


@then('the error message should indicate card expiration')
def step_verify_card_expiration_error(context):
    """Verify error indicates card expiration"""
    response_data = context.response.json()
    error_msg = str(response_data).lower()
    assert 'expir' in error_msg or 'expired' in error_msg
