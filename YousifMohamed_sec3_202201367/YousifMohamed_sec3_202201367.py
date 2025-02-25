# -*- coding: utf-8 -*-
"""Copy of Lab 10 Colab practice and requirements.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vzgXrsztL6r1rhAY28v54TeXdHpEgr3r

# LAB 10 : UNIT TESTING


---

In this lab, we will learn the core concepts of Unit Testing in software development. The purpose of Unit Testing is to validate that individual units of source code, such as functions, methods, or classes, work as intended. Unit testing ensures that small, isolated components of a program behave correctly under different scenarios. Writing unit tests helps developers catch bugs early in the development cycle and maintain code reliability.

**What is a Unit ?**

A unit refers to the smallest testable part of an application. This could be a function, method, or class that performs a specific task. The goal of unit testing is to ensure that each unit works in isolation without depending on other parts of the program.

**Assertions in Unit Testing**

Assertions are conditions or boolean expressions that evaluate whether the output of a unit matches the expected result.

##**Running Tests Directly (Without unittest)**

For example:
"""

import unittest
def add(a, b):
    return a + b

# Unit test
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    print("All tests passed!")
if __name__ == "__main__":
    test_add()

"""Here, the assert statement verifies that the add function returns the correct result for various inputs. If the assertion fails, the test reports an error, helping identify issues in the code.

## **Running Tests Using unittest Framework**

Example using Python’s unittest:

Failing tests:
"""

import unittest
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 4)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""Successfull tests:"""

import unittest
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""or use this line:"""

unittest.main(argv=[''], exit=False)

"""Here, the unittest.TestCase class provides methods like assertEqual to validate the output of the function being tested.

**Mocking in Unit Testing**

Mocking is a technique used to replace real components (like databases, APIs, or external systems) with simulated versions during testing. This allows you to test a unit in isolation without relying on external dependencies.
Example using Python’s unittest.mock:

directly:
"""

from unittest.mock import Mock

# Mocking an external API call
api_mock = Mock(return_value={"status": "success", "data": []})
response = api_mock()

assert response["status"] == "success"
print("Test passed!")

"""with unittest framework:"""

import unittest
from unittest.mock import Mock

class TestAPIMock(unittest.TestCase):
    def test_api_mock(self):
        # Mocking an external API call
        api_mock = Mock(return_value={"status": "success", "data": []})
        response = api_mock()

        # Assertions
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["data"], [])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""**Example Problem:**

Write a Python function to calculate the factorial of a number and create unit tests for the function.

"""

import unittest

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Unit test class
class TestFactorialFunction(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)  # Factorial of 0
        self.assertEqual(factorial(1), 1)  # Factorial of 1
        self.assertEqual(factorial(5), 120)  # Factorial of 5
        self.assertEqual(factorial(10), 3628800)  # Factorial of 10

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""Explanation:

In this example:

The factorial function is the unit under test.
The unit tests validate that the function produces correct results for edge cases (n=0, n=1) and general cases (n=5, n=10).

# **Practice:**

1.Analyze and Debug a Unit Test

Below is a unit test written for the function divide_numbers(a, b):
"""

def divide_numbers(a, b):
    return a / b
# Unit test
def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(5, 0) == "Undefined"  # This is expected to fail
    assert divide_numbers(0, 5) == 0
    print("passed")

test_divide_numbers()

"""Write your corrected code below:"""



"""2.Write unit tests for the following functions:"""

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

"""
Tasks:

Test the subtract function with positive, negative, and zero values.

Test the divide function with:

Normal inputs.

Division by zero (should raise an exception)."""



"""# Requirement

## 1. Write Unit Tests from Scratch

###Function 1: multiply_numbers(a, b)

Write a function that multiplies two numbers and test for:

Two positive numbers.

Multiplication with zero.

Negative numbers.
"""

import unittest
def multiply_numbers(a,b):
    return a*b

class TestMultiplyNumbers(unittest.TestCase):
    def test_mulyiply(self):
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(-3, 4), -12)
        self.assertEqual(multiply_numbers(-3, -4), 12)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""###Function 2: reverse_list(input_list)

Write a function that reverses a given list and test for:

A normal list.

An empty list.

A single-element list.


"""

import unittest

def reverse_list(input_list):
    return input_list[::-1]

class TestReverseList(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([42]), [42])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""##2. Extend Provided Code

Function 3: calculate_discount(price, discount_percentage)

Extend the function by:

Adding a test for valid inputs (e.g., price = 100, discount = 10%).

Testing invalid discounts (negative or greater than 100%).

Handling zero price or zero discount.


"""

import unittest

def calculate_discount(price, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("must be between 0 and 100.")
    if price < 0:
        raise ValueError("cannot be negative.")
    return price - (price * discount_percentage / 100)

class TestCalculateDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)
        self.assertEqual(calculate_discount(200, 25), 150)
        self.assertEqual(calculate_discount(0, 10), 0)
        self.assertEqual(calculate_discount(100, 0), 100)
    def test_invalid_discount_negative(self):
        with self.assertRaises(ValueError): calculate_discount(100, -10)
    def test_invalid_discount_over_100(self):
        with self.assertRaises(ValueError): calculate_discount(100, 110)
    def test_negative_price(self):
        with self.assertRaises(ValueError):calculate_discount(-100, 10)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""##3. Encapsulate in a Class


Class: MathOperations

Implement a class MathOperations that contains:

Method 1: is_prime(n)

Check if a number is prime.

Test cases:

Prime numbers.

Non-prime numbers.

Edge cases like 0, 1, and negative numbers.

Method 2: factorial(n)

Compute the factorial of a number.

Test cases:

Positive integers.

Edge case: n = 0 (factorial is 1).

Invalid cases: negative numbers.
"""

import unittest

class MathOperations:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()
    def test_is_prime(self):
        self.assertTrue(self.math_ops.is_prime(2))
        self.assertTrue(self.math_ops.is_prime(3))
        self.assertTrue(self.math_ops.is_prime(17))
        self.assertFalse(self.math_ops.is_prime(4))
        self.assertFalse(self.math_ops.is_prime(9))
        self.assertFalse(self.math_ops.is_prime(0))
        self.assertFalse(self.math_ops.is_prime(1))
        self.assertFalse(self.math_ops.is_prime(-5))
    def test_factorial(self):
        self.assertEqual(self.math_ops.factorial(5), 120)
        self.assertEqual(self.math_ops.factorial(10), 3628800)
        self.assertEqual(self.math_ops.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.math_ops.factorial(-1)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)