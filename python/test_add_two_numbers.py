import pytest
from adder import add_two_numbers

def test_add_two_positive_integers():
    assert add_two_numbers(3, 2) == 5, "Should be 5"

def test_add_negative_and_positive_integer():
    assert add_two_numbers(-1, 1) == 0, "Should be 0"

def test_add_two_floats():
    assert add_two_numbers(1.1, 2.2) == 3.3, "Should be 3.3"

def test_add_integer_and_float():
    assert add_two_numbers(5, 2.5) == 7.5, "Should be 7.5"
