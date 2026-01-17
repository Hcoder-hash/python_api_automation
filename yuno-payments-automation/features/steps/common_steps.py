"""
Common step definitions for all feature tests
"""
from behave import given, when, then
import requests
from context_manager import ContextManager


@given('the API is available at the configured endpoint')
def step_api_available(context):
    """Verify that the API endpoint is available"""
    context.manager = ContextManager()
    context.api_url = context.manager.get_api_url()
    try:
        response = requests.get(f"{context.api_url}/health", timeout=5)
        assert response.status_code == 200, "API is not available"
        context.api_healthy = True
    except Exception as e:
        context.api_healthy = False
        raise AssertionError(f"API health check failed: {str(e)}")


@then('the HTTP status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    """Verify the HTTP response status code"""
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, got {context.response.status_code}"


@then('the response should contain a valid JSON')
def step_verify_json_response(context):
    """Verify the response is valid JSON"""
    try:
        context.response_json = context.response.json()
    except ValueError as e:
        raise AssertionError(f"Response is not valid JSON: {str(e)}")


@then('the error message should indicate {error_type}')
def step_verify_error_message(context, error_type):
    """Verify error message contains specific error type"""
    response_data = context.response.json()
    error_message = response_data.get('message', '').lower()
    assert error_type.lower() in error_message, \
        f"Error message does not contain '{error_type}'"
