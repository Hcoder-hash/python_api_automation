# Yuno Payments Automation - Quick Start Guide

## Setup Instructions

### 1. Environment Setup
```bash
cp .env.example .env

# Edit .env with your API credentials
# API_URL=https://your-api-endpoint.com
# API_KEY=your_actual_api_key
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Tests
```bash
# Run all tests
behave

# Run specific feature
behave features/purchase.feature

# Run with detailed output
behave -v

# Generate HTML report
behave --format html -o report.html
```

## Project Structure Summary

```
├── features/              - BDD test scenarios (Gherkin)
│   ├── steps/            - Step implementations
│   └── environment.py    - Test hooks and setup
├── core/                 - Core automation components
│   ├── api_client.py     - HTTP client
│   ├── request_builder.py - Request payloads
│   └── response_validator.py - Response validation
├── test_data/            - Test data (cards, amounts, etc)
├── docs/                 - Documentation
└── requirements.txt      - Python dependencies
```

## Key Features

✅ BDD Framework (Behave)  
✅ Comprehensive API Testing  
✅ Retry Logic & Session Management  
✅ Request/Response Validation  
✅ JSON Schema Validation  
✅ Detailed Test Documentation  
✅ CI/CD Ready  

## Common Commands

| Command | Purpose |
|---------|---------|
| `behave` | Run all tests |
| `behave features/purchase.feature` | Run specific feature |
| `behave -v` | Verbose output |
| `behave --no-capture` | Show print statements |
| `behave --format json -o report.json` | JSON report |
| `behave --dry-run` | Validate syntax |

## Troubleshooting

**Import Error**: Ensure you're in the project directory and venv is activated  
**Connection Error**: Check API_URL and API_KEY in .env  
**Test Failures**: Review response logs and scenario details  

See `docs/Test_Cases.md` for detailed test documentation.
