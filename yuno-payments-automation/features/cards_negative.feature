Feature: Card Payment Negative Tests
  As a QA engineer
  I want to validate error handling for invalid cards
  So that the system handles edge cases properly

  Background:
    Given the API is available at the configured endpoint

  Scenario: Payment with invalid card number
    When I attempt to process payment with invalid card number
    Then the API should reject the request
    And the error should indicate invalid card number
    And the HTTP status code should be 400

  Scenario: Payment with expired card
    When I attempt to process payment with expired card
    Then the API should reject the request
    And the error message should indicate card expiration
    And the payment should not be processed

  Scenario: Payment with invalid CVV
    When I attempt to process payment with invalid CVV
    Then the API should reject the request
    And the error message should indicate invalid CVV
    And the HTTP status code should be 400

  Scenario: Payment with insufficient funds
    When I attempt to process payment with insufficient funds card
    Then the payment should be declined
    And the error should indicate insufficient funds
    And the transaction should not be created

  Scenario: Payment with stolen card
    When I attempt to process payment with flagged card
    Then the payment should be declined
    And the error should indicate card blocked
    And the transaction should not be created
