# Test Cases Documentation

## Payment API Test Cases

### 1. Purchase Operations

#### TC-001: Successful Payment Purchase
- **Objective**: Verify successful payment processing with valid card
- **Preconditions**: 
  - API endpoint is available
  - Valid merchant credentials configured
  - Test card data available
- **Steps**:
  1. Create purchase request with valid card details
  2. Send POST request to `/payments/purchase`
  3. Verify HTTP response is 200
  4. Verify transaction ID is returned
  5. Verify payment status is COMPLETED
- **Expected Result**: Payment processed successfully
- **Test Data**: Valid Visa card (4532015112830366)

#### TC-002: Purchase with Missing Fields
- **Objective**: Validate error handling for incomplete requests
- **Preconditions**: API endpoint available
- **Steps**:
  1. Create purchase request without required fields
  2. Send POST request
  3. Verify HTTP status code is 400
  4. Verify validation error message
- **Expected Result**: API rejects request with 400 Bad Request
- **Test Data**: Incomplete payment payload

#### TC-003: Purchase with Invalid Amount
- **Objective**: Verify validation of payment amount
- **Preconditions**: API endpoint available
- **Steps**:
  1. Create purchase with amount = 0
  2. Send POST request
  3. Verify rejection
- **Expected Result**: API rejects with validation error

### 2. Authorization Operations

#### TC-004: Successful Payment Authorization
- **Objective**: Verify successful payment authorization
- **Preconditions**: API available, valid card data
- **Steps**:
  1. Send authorization request with valid card
  2. Verify HTTP 200 response
  3. Verify authorization code returned
  4. Verify status is AUTHORIZED
- **Expected Result**: Payment authorized successfully

#### TC-005: Authorization with Insufficient Funds
- **Objective**: Verify decline for insufficient funds
- **Preconditions**: API available
- **Steps**:
  1. Authorize with insufficient funds test card
  2. Verify HTTP 402 response
  3. Verify error message indicates insufficient funds
- **Expected Result**: Authorization declined

#### TC-006: Authorization with Expired Card
- **Objective**: Verify decline for expired cards
- **Preconditions**: API available
- **Steps**:
  1. Authorize with expired test card
  2. Verify failure
  3. Verify error indicates expiration
- **Expected Result**: Authorization declined

### 3. Refund Operations

#### TC-007: Full Refund Processing
- **Objective**: Verify full refund of completed payment
- **Preconditions**: 
  - API available
  - Payment already completed
- **Steps**:
  1. Create refund request for completed transaction
  2. Set refund amount equal to original
  3. Submit refund request
  4. Verify HTTP 200 response
  5. Verify refund transaction ID
  6. Verify status is REFUNDED
- **Expected Result**: Full refund processed successfully

#### TC-008: Partial Refund Processing
- **Objective**: Verify partial refund capability
- **Preconditions**: Payment already completed
- **Steps**:
  1. Create partial refund request
  2. Set refund amount less than original
  3. Submit request
  4. Verify success
  5. Verify status is PARTIALLY_REFUNDED
- **Expected Result**: Partial refund processed

#### TC-009: Refund Invalid Transaction
- **Objective**: Verify error handling for invalid transactions
- **Preconditions**: API available
- **Steps**:
  1. Request refund with non-existent transaction ID
  2. Verify HTTP 404 response
- **Expected Result**: API returns not found error

### 4. Cancellation Operations

#### TC-010: Cancel Authorized Payment
- **Objective**: Verify cancellation of authorized payment
- **Preconditions**: Payment authorized but not captured
- **Steps**:
  1. Authorize payment
  2. Submit cancellation request
  3. Verify success
  4. Verify status is CANCELLED
- **Expected Result**: Payment cancelled successfully

#### TC-011: Cancel Captured Payment
- **Objective**: Verify denial of cancellation for captured payments
- **Preconditions**: Payment already captured
- **Steps**:
  1. Attempt to cancel captured payment
  2. Verify HTTP 409 Conflict response
  3. Verify error message
- **Expected Result**: Cancellation denied with conflict error

#### TC-012: Cancel Invalid Transaction
- **Objective**: Verify error for non-existent transaction
- **Preconditions**: API available
- **Steps**:
  1. Submit cancellation with invalid ID
  2. Verify HTTP 404 response
- **Expected Result**: Not found error returned

### 5. Verification Operations

#### TC-013: Verify Completed Payment
- **Objective**: Retrieve details of completed payment
- **Preconditions**: Payment completed
- **Steps**:
  1. Send verification request with transaction ID
  2. Verify HTTP 200 response
  3. Verify all payment details returned
- **Expected Result**: Payment details retrieved successfully

#### TC-014: Verify Invalid Transaction
- **Objective**: Error handling for non-existent transactions
- **Preconditions**: API available
- **Steps**:
  1. Verify with non-existent transaction ID
  2. Verify HTTP 404 response
- **Expected Result**: Not found error returned

#### TC-015: Verify Missing Transaction ID
- **Objective**: Validation of required parameters
- **Preconditions**: API available
- **Steps**:
  1. Submit verification without transaction ID
  2. Verify HTTP 400 response
- **Expected Result**: Validation error returned

### 6. Customer Management

#### TC-016: Create Customer Profile
- **Objective**: Create new customer record
- **Preconditions**: API available
- **Steps**:
  1. Submit customer creation request with valid data
  2. Verify HTTP 201/200 response
  3. Verify customer ID returned
  4. Verify status is ACTIVE
- **Expected Result**: Customer created successfully

#### TC-017: Retrieve Customer Details
- **Objective**: Fetch customer information
- **Preconditions**: Customer exists
- **Steps**:
  1. Request customer by ID
  2. Verify HTTP 200 response
  3. Verify all customer details returned
- **Expected Result**: Customer details retrieved

#### TC-018: Update Customer Profile
- **Objective**: Modify customer information
- **Preconditions**: Customer exists
- **Steps**:
  1. Submit update request with new data
  2. Verify HTTP 200 response
  3. Verify changes applied
- **Expected Result**: Customer updated successfully

#### TC-019: Delete Customer Profile
- **Objective**: Deactivate customer account
- **Preconditions**: Customer exists
- **Steps**:
  1. Submit delete request
  2. Verify HTTP 200/204 response
  3. Verify status is INACTIVE
- **Expected Result**: Customer deleted/deactivated

### 7. Negative Test Cases (Invalid Cards)

#### TC-020: Invalid Card Number
- **Objective**: Reject payment with invalid card number
- **Preconditions**: API available
- **Steps**:
  1. Process payment with invalid card number
  2. Verify HTTP 400 response
- **Expected Result**: Payment rejected

#### TC-021: Expired Card Payment
- **Objective**: Reject expired cards
- **Preconditions**: API available
- **Steps**:
  1. Process payment with expired card
  2. Verify rejection
- **Expected Result**: Payment declined

#### TC-022: Invalid CVV
- **Objective**: Reject invalid CVV codes
- **Preconditions**: API available
- **Steps**:
  1. Process payment with invalid CVV
  2. Verify HTTP 400 response
- **Expected Result**: Payment rejected

#### TC-023: Insufficient Funds
- **Objective**: Handle insufficient funds scenario
- **Preconditions**: API available
- **Steps**:
  1. Process payment with insufficient funds card
  2. Verify decline
- **Expected Result**: Payment declined

#### TC-024: Stolen/Flagged Card
- **Objective**: Block flagged/stolen cards
- **Preconditions**: API available
- **Steps**:
  1. Process payment with blocked card
  2. Verify rejection
- **Expected Result**: Payment declined and flagged

## Test Execution Strategy

### Execution Order
1. Basic connectivity test (TC-001 first step)
2. Customer management tests (TC-016 to TC-019)
3. Payment operations (TC-001 to TC-003)
4. Authorization tests (TC-004 to TC-006)
5. Capture/Verification (TC-013 to TC-015)
6. Refund tests (TC-007 to TC-009)
7. Cancellation tests (TC-010 to TC-012)
8. Negative tests (TC-020 to TC-024)

### Success Criteria
- All HTTP status codes match expected values
- All required fields present in responses
- Response payloads validate against schemas
- Error messages are clear and actionable
- No unhandled exceptions in API

## Test Data Requirements
- Valid credit card numbers (multiple brands)
- Invalid/expired card numbers
- Test amounts (100, 9999, 999999)
- Customer data (names, emails, phone)
- Valid transaction IDs from previous runs

## Environment Setup
- API URL configured
- Authentication credentials available
- Test data loaded
- Schema files accessible
- Logging enabled for debugging
