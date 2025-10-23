Feature: Calculator
  As a user
  I want to perform basic arithmetic operations
  So that I can calculate results

  Scenario: Add two numbers
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5

  Scenario: Subtract two numbers
    Given I have a calculator
    When I subtract 3 from 5
    Then the result should be 2

  Scenario: Multiply two numbers
    Given I have a calculator
    When I multiply 4 and 3
    Then the result should be 12

  Scenario: Divide two numbers
    Given I have a calculator
    When I divide 10 by 2
    Then the result should be 5

  Scenario: Division by zero
    Given I have a calculator
    When I divide 10 by 0
    Then I should get an error

  Scenario Outline: Add multiple numbers
    Given I have a calculator
    When I add <a> and <b>
    Then the result should be <result>

    Examples:
      | a  | b  | result |
      | 1  | 2  | 3      |
      | -1 | 1  | 0      |
      | 0  | 5  | 5      |
