"""
Behave environment configuration for test setup and teardown
"""
import os
import json
from core.api_client import APIClient


def before_all(context):
    """Setup before all tests"""
    context.config = {
        'api_url': os.getenv('API_URL', 'https://api.yuno.test'),
        'api_key': os.getenv('API_KEY', 'test_key'),
        'timeout': 30,
        'verify_ssl': False
    }
    context.api_client = APIClient(context.config)


def before_scenario(context, scenario):
    """Setup before each scenario"""
    context.scenario_name = scenario.name
    context.test_data = {}
    context.response = None
    context.request_payload = None
    print(f"\n\nStarting Scenario: {scenario.name}")


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    print(f"Completed Scenario: {scenario.name}")
    if scenario.status == 'failed':
        print(f"Scenario failed with status: {scenario.status}")
        if hasattr(context, 'response') and context.response:
            try:
                print(f"Response: {context.response.text}")
            except:
                pass


def after_all(context):
    """Cleanup after all tests"""
    print("\n\nAll tests completed")
