Feature: Payment Cancellation
  As a merchant
  I want to cancel authorized payments
  So that I can prevent payment processing when needed

  Background:
    Given the API is available at the configured endpoint

  Scenario: Successful cancellation of authorized payment
    When I authorize a payment
    And I cancel the authorized payment
    Then the cancellation should be successful
    And the payment status should be CANCELLED
    And the authorization should be voided

  Scenario: Cancel already captured payment
    When I attempt to cancel an already captured payment
    Then the cancellation should fail
    And the error message should indicate payment already captured
    And the HTTP status code should be 409

  Scenario: Cancel with invalid transaction ID
    When I attempt to cancel with an invalid transaction ID
    Then the API should return a not found error
    And the HTTP status code should be 404
