Feature: Payment Refund Operations
  As a merchant
  I want to refund payments to customers
  So that I can handle customer returns and cancellations

  Background:
    Given the API is available at the configured endpoint

  Scenario: Successful full refund
    When I create a refund request for a completed payment
    And the refund amount equals the original payment amount
    Then the refund should be processed successfully
    And the response should contain a refund transaction ID
    And the payment status should be REFUNDED

  Scenario: Successful partial refund
    When I create a partial refund request
    And the refund amount is less than the original payment
    Then the partial refund should be processed successfully
    And the remaining balance should be reflected
    And the payment status should be PARTIALLY_REFUNDED

  Scenario: Refund with invalid transaction ID
    When I attempt to refund with an invalid transaction ID
    Then the API should return a not found error
    And the HTTP status code should be 404
