Feature: Payment Verification
  As a merchant
  I want to verify payment status and details
  So that I can confirm transaction information

  Background:
    Given the API is available at the configured endpoint

  Scenario: Verify completed payment
    When I verify a completed payment transaction
    And I provide the valid transaction ID
    Then the verification should be successful
    And the response should contain complete payment details
    And the status should match the original transaction

  Scenario: Verify with invalid transaction ID
    When I attempt to verify with a non-existent transaction ID
    Then the verification should fail
    And the HTTP status code should be 404
    And the error message should indicate transaction not found

  Scenario: Verify payment with missing transaction ID
    When I attempt to verify without providing transaction ID
    Then the API should return a validation error
    And the HTTP status code should be 400
