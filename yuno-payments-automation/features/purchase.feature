Feature: Payment Purchase Operations
  As a merchant
  I want to process payments successfully
  So that I can accept customer payments

  Background:
    Given the API is available at the configured endpoint

  Scenario: Successful payment purchase with valid card
    When I create a purchase request with valid card details
    And the request contains the required payment information
    Then the purchase should be processed successfully
    And the response should contain a valid transaction ID
    And the payment status should be COMPLETED

  Scenario: Purchase request with missing fields
    When I create a purchase request without required fields
    Then the API should return a validation error
    And the error message should indicate missing fields
    And the HTTP status code should be 400

  Scenario: Purchase with invalid amount
    When I create a purchase request with amount of 0
    Then the API should reject the request
    And the response should contain validation error message
