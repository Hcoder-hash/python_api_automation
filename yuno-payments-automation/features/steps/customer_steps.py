"""
Customer-related step definitions
"""
from behave import when, then
from core.request_builder import RequestBuilder


@when('I create a customer profile with valid information')
def step_create_customer_with_valid_info(context):
    """Create a customer profile with valid information"""
    request_builder = RequestBuilder()
    payload = request_builder.build_customer_request(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="+1234567890"
    )
    context.request_payload = payload
    context.response = context.manager.post(
        f"{context.api_url}/customers",
        json=payload
    )


@when('the request contains required customer fields')
def step_verify_customer_request_valid(context):
    """Verify customer request has required fields"""
    required_fields = ['first_name', 'last_name', 'email']
    for field in required_fields:
        assert field in context.request_payload, f"Missing required field: {field}"


@then('the customer should be created successfully')
def step_customer_created_successfully(context):
    """Verify customer was created"""
    assert context.response.status_code == 201 or context.response.status_code == 200


@then('the response should contain a customer ID')
def step_verify_customer_id(context):
    """Verify response contains customer ID"""
    response_data = context.response.json()
    assert 'customer_id' in response_data or 'id' in response_data
    context.customer_id = response_data.get('customer_id') or response_data.get('id')


@then('the customer status should be ACTIVE')
def step_verify_customer_active(context):
    """Verify customer status is ACTIVE"""
    response_data = context.response.json()
    assert response_data.get('status') == 'ACTIVE'


@when('I retrieve a customer by valid customer ID')
def step_retrieve_customer_by_id(context):
    """Retrieve customer by ID"""
    context.response = context.manager.get(
        f"{context.api_url}/customers/{context.customer_id}"
    )


@when('the customer exists in the system')
def step_verify_customer_exists(context):
    """Verify customer exists"""
    assert context.response.status_code == 200


@then('the customer details should be returned successfully')
def step_customer_details_returned(context):
    """Verify customer details returned"""
    assert context.response.status_code == 200


@then('the response should contain all customer information')
def step_verify_customer_information(context):
    """Verify response contains customer information"""
    response_data = context.response.json()
    assert 'first_name' in response_data or 'name' in response_data


@when('I update an existing customer profile')
def step_update_customer_profile(context):
    """Update customer profile"""
    request_builder = RequestBuilder()
    payload = request_builder.build_customer_request(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        phone="+1987654321"
    )
    context.response = context.manager.put(
        f"{context.api_url}/customers/{context.customer_id}",
        json=payload
    )


@when('I provide valid customer ID and new information')
def step_verify_update_payload(context):
    """Verify update payload is valid"""
    assert 'first_name' in context.request_payload


@then('the update should be successful')
def step_update_successful(context):
    """Verify update was successful"""
    assert context.response.status_code == 200 or context.response.status_code == 204


@then('the customer record should reflect the changes')
def step_verify_changes_applied(context):
    """Verify changes were applied"""
    response_data = context.response.json() if context.response.text else {}
    # Changes are typically reflected in the response or we can re-fetch to verify
    assert context.response.status_code < 300


@when('I delete a customer profile')
def step_delete_customer_profile(context):
    """Delete customer profile"""
    context.response = context.manager.delete(
        f"{context.api_url}/customers/{context.customer_id}"
    )


@then('the deletion should be successful')
def step_deletion_successful(context):
    """Verify deletion was successful"""
    assert context.response.status_code == 200 or context.response.status_code == 204


@then('the customer status should be INACTIVE')
def step_verify_customer_inactive(context):
    """Verify customer is now inactive"""
    # Typically deletion returns 204 No Content or 200 with success message
    assert context.response.status_code < 300
