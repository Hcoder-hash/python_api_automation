Feature: Payment Authorization
  As a merchant
  I want to authorize payments before capturing
  So that I can validate payments before processing

  Background:
    Given the API is available at the configured endpoint

  Scenario: Successful payment authorization
    When I authorize a payment with valid card details
    And the authorization request is valid
    Then the authorization should be successful
    And the response should contain an authorization code
    And the payment status should be AUTHORIZED

  Scenario: Authorization with insufficient funds
    When I authorize a payment with insufficient funds card
    Then the authorization should fail
    And the response should indicate insufficient funds
    And the HTTP status code should be 402

  Scenario: Authorization with expired card
    When I authorize a payment with expired card
    Then the authorization should fail
    And the error message should indicate card expiration
