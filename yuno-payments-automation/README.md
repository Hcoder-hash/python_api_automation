# Yuno Payments Automation Framework

## Overview
This is a BDD (Behavior-Driven Development) test automation framework for the Yuno Payments API. It uses Behave (Python's Gherkin implementation) for writing readable test scenarios and provides comprehensive API testing capabilities.

## Project Structure

```
yuno-payments-automation/
├── README.md                          # This file
├── features/                          # Feature files (Gherkin syntax)
│   ├── purchase.feature               # Payment purchase scenarios
│   ├── authorization.feature          # Payment authorization scenarios
│   ├── refund.feature                 # Refund operation scenarios
│   ├── cancel.feature                 # Payment cancellation scenarios
│   ├── verify.feature                 # Payment verification scenarios
│   ├── customer.feature               # Customer management scenarios
│   ├── cards_negative.feature         # Negative test scenarios
│   ├── environment.py                 # Behave environment hooks
│   └── steps/                         # Step definitions
│       ├── common_steps.py            # Common/shared step implementations
│       ├── payment_steps.py           # Payment-related step implementations
│       └── customer_steps.py          # Customer-related step implementations
├── core/                              # Core automation components
│   ├── api_client.py                  # HTTP client with retry logic
│   ├── request_builder.py             # Request payload builder
│   ├── response_validator.py          # Response validation utilities
│   └── schema/                        # JSON schemas for validation
│       ├── payment_schema.json        # Payment response schema
│       └── refund_schema.json         # Refund response schema
├── test_data/                         # Test data files
│   ├── valid_cards.json               # Valid card test data
│   └── invalid_cards.json             # Invalid card test data
└── docs/                              # Documentation
    └── Test_Cases.md                  # Detailed test case documentation
```

## Prerequisites

### System Requirements
- Python 3.7 or higher
- pip (Python package manager)
- Windows/Linux/macOS

### Python Dependencies
```
behave==1.2.6
requests==2.28.2
urllib3==1.26.14
jsonschema==4.17.3
python-dotenv==0.21.0
```

## Installation

### 1. Clone or Extract Project
```bash
cd path/to/yuno-payments-automation
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install behave requests urllib3 jsonschema python-dotenv
```

## Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
API_URL=https://api.yuno.test
API_KEY=your_api_key_here
TIMEOUT=30
VERIFY_SSL=False
```

### API Client Configuration
Edit `features/environment.py` to modify:
- Base API URL
- Authentication method
- Timeout settings
- SSL verification

## Running Tests

### Run All Tests
```bash
behave
```

### Run Specific Feature File
```bash
behave features/purchase.feature
```

### Run Tests with Tags
```bash
behave -t @payment
behave -t @negative
```

### Run with Detailed Output
```bash
behave -v
```

### Run with Logging
```bash
behave --no-capture
```

### Generate Reports
```bash
behave --format json -o report.json
behave --format html -o report.html
```

## Feature Files Overview

### 1. Purchase Operations (`purchase.feature`)
- Successful payment purchase with valid card
- Purchase with missing required fields
- Purchase with invalid amounts

**Scenarios**: 3  
**Focus**: Payment creation and validation

### 2. Authorization (`authorization.feature`)
- Successful payment authorization
- Authorization with insufficient funds
- Authorization with expired card

**Scenarios**: 3  
**Focus**: Authorization flows and error handling

### 3. Refunds (`refund.feature`)
- Successful full refund
- Successful partial refund
- Refund with invalid transaction ID

**Scenarios**: 3  
**Focus**: Refund processing

### 4. Cancellation (`cancel.feature`)
- Successful cancellation of authorized payment
- Cancellation of already captured payment
- Cancellation with invalid transaction ID

**Scenarios**: 3  
**Focus**: Payment cancellation

### 5. Verification (`verify.feature`)
- Verify completed payment
- Verify with invalid transaction ID
- Verify with missing transaction ID

**Scenarios**: 3  
**Focus**: Transaction verification

### 6. Customer Management (`customer.feature`)
- Create new customer profile
- Retrieve customer details
- Update customer profile
- Delete customer profile

**Scenarios**: 4  
**Focus**: Customer CRUD operations

### 7. Card Negative Tests (`cards_negative.feature`)
- Invalid card number
- Expired card
- Invalid CVV
- Insufficient funds
- Stolen/flagged card

**Scenarios**: 5  
**Focus**: Error handling and edge cases

## Step Definitions

### Common Steps (`common_steps.py`)
```gherkin
Given the API is available at the configured endpoint
Then the HTTP status code should be {status_code}
Then the response should contain a valid JSON
Then the error message should indicate {error_type}
```

### Payment Steps (`payment_steps.py`)
```gherkin
When I create a purchase request with valid card details
When I authorize a payment with valid card details
When I create a refund request for a completed payment
...and many more
```

### Customer Steps (`customer_steps.py`)
```gherkin
When I create a customer profile with valid information
When I retrieve a customer by valid customer ID
When I update an existing customer profile
When I delete a customer profile
...
```

## API Endpoints

The framework tests the following endpoints:

### Health Check
- `GET /health` - Verify API availability

### Payments
- `POST /payments/purchase` - Process payment
- `POST /payments/authorize` - Authorize payment
- `POST /payments/refund` - Refund payment
- `POST /payments/cancel` - Cancel payment
- `GET /payments/{transaction_id}` - Verify payment

### Customers
- `POST /customers` - Create customer
- `GET /customers/{customer_id}` - Retrieve customer
- `PUT /customers/{customer_id}` - Update customer
- `DELETE /customers/{customer_id}` - Delete customer

## Test Data

### Valid Cards (test_data/valid_cards.json)
- Visa: 4532015112830366
- Mastercard: 5425233010103442
- American Express: 378282246310005
- Discover: 6011111111111117

### Invalid Cards (test_data/invalid_cards.json)
- Insufficient Funds: 4000000000000002
- Expired: 4000000000000069
- Lost/Flagged: 4000000000000127
- Stolen: 4000000000000035

## Core Components

### APIClient (`core/api_client.py`)
HTTP client with:
- Automatic retry logic
- Session management
- Header management
- Timeout handling
- SSL verification options

### RequestBuilder (`core/request_builder.py`)
Builds various request payloads:
- `build_purchase_request()` - Purchase payment
- `build_authorization_request()` - Authorize payment
- `build_refund_request()` - Refund payment
- `build_cancellation_request()` - Cancel payment
- `build_customer_request()` - Customer creation
- `build_verification_request()` - Payment verification

### ResponseValidator (`core/response_validator.py`)
Validates API responses:
- JSON schema validation
- Status code validation
- Required fields validation
- Field type validation
- Field value validation

## Hooks and Fixtures

### Before All
- Initialize API client and configuration

### Before Scenario
- Set up test context
- Initialize response and payload holders
- Print scenario name

### After Scenario
- Cleanup after test execution
- Print results and errors

### After All
- Final cleanup
- Print summary

## Logging and Debugging

### Enable Detailed Logging
```bash
behave --no-capture
```

### Check Response Content
Steps automatically log response data on failure.

### Common Issues

**Issue**: API connection timeout  
**Solution**: Increase TIMEOUT in environment.py

**Issue**: SSL certificate errors  
**Solution**: Set VERIFY_SSL=False for testing environments

**Issue**: Authentication failures  
**Solution**: Verify API_KEY in .env file

## Contributing

### Adding New Scenarios
1. Create feature file in `features/` directory
2. Write Gherkin scenarios
3. Implement corresponding steps in `features/steps/`
4. Update documentation

### Adding New Step Definitions
1. Create method with `@when`, `@then`, `@given` decorators
2. Use BDD-style naming
3. Add docstrings
4. Handle exceptions gracefully

### Code Style
- PEP 8 compliance
- Clear variable naming
- Comprehensive docstrings
- Proper error handling

## Performance Optimization

### Parallel Execution
To run tests in parallel:
```bash
pip install behave-parallel
behave-parallel --max-workers 4
```

### Test Execution Strategy
- Run health checks first
- Execute customer tests before payment tests
- Group related scenarios
- Run negative tests last

## Troubleshooting

### Tests Not Running
```bash
# Verify behave installation
pip show behave

# Check feature file syntax
behave --dry-run
```

### Connection Issues
```bash
# Test API connectivity
python -c "import requests; requests.get('API_URL')"
```

### Import Errors
```bash
# Verify PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/project"
```

## CI/CD Integration

### GitHub Actions Example
```yaml
- name: Run Tests
  run: |
    pip install -r requirements.txt
    behave
```

### Jenkins Example
```groovy
stage('Test') {
    steps {
        sh 'pip install -r requirements.txt'
        sh 'behave'
    }
}
```

## Resources

- [Behave Documentation](https://behave.readthedocs.io/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/reference/)
- [API Testing Best Practices](https://www.soapui.org/)
- [JSON Schema Validation](https://json-schema.org/)

## Support

For issues or questions:
1. Check the Test_Cases.md documentation
2. Review step definitions in features/steps/
3. Check API response logs
4. Verify environment configuration

## License

This project is provided as-is for testing purposes.

## Version History

### v1.0.0 (Initial Release)
- Core API client implementation
- Payment operations testing
- Customer management testing
- Comprehensive test scenarios
- Request/response validation

---

**Last Updated**: January 2025  
**Framework Version**: 1.0.0
