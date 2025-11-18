# Homework
Name: Connor Chen

## Question 1) Define the following unit, integration, regression tests and when you would use each?
Unit Test: 
A unit test is when developers test a unit of code. It tests a piece of code to check if it functions correctly. 
You would use a unit test when you want to confirm individual parts of your code work correctly on their own. 

Integration Test:
An integration test is when developers test how well thier uhnjits work together with other units. It essentially checks how multiple components work together. 
You would use an integration tests to make sure multiple parts of the system interact properly.

Regression Test: 
A regression test re-runs previous test to ensure that latest code changes do not break anything. It essentially checks that multiple parts of your code work together.
You would use a regresion test when you change a your code and want to make sure previous parts of your code is working properly.

## Question 2) Breifly explain pytest discovery (file/funciont naming) and what a fixture is.
Pytest discover is a python testing framework that identifies and collect test files, functions, and classes within a project. It finds and runs tests based on naming convention. For example, test files must be named _test_*.py_ or _*_test.py_ and test functions must be named _test..._. Once the tests are discovered, Pytest can executed and it will discover test files, run them, and reports any failures.

