Feature: Customer Management
  As a merchant
  I want to manage customer profiles
  So that I can store and retrieve customer information

  Background:
    Given the API is available at the configured endpoint

  Scenario: Create new customer profile
    When I create a customer profile with valid information
    And the request contains required customer fields
    Then the customer should be created successfully
    And the response should contain a customer ID
    And the customer status should be ACTIVE

  Scenario: Retrieve customer details
    When I retrieve a customer by valid customer ID
    And the customer exists in the system
    Then the customer details should be returned successfully
    And the response should contain all customer information

  Scenario: Update customer profile
    When I update an existing customer profile
    And I provide valid customer ID and new information
    Then the update should be successful
    And the customer record should reflect the changes

  Scenario: Delete customer profile
    When I delete a customer profile
    And the customer ID is valid
    Then the deletion should be successful
    And the customer status should be INACTIVE
