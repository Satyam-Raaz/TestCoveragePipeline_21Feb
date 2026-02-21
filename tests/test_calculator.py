# test_calculator.py
# import pytest
# from calculator import add, subtract, multiply, divide


# tests/test_calculator.py

import pytest

import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


@pytest.fixture
def calc():
  return Calculator()


# --- Basic Tests ---
def test_add(calc):
  assert calc.add(2, 3) == 5
  assert calc.add(-1, 1) == 0


def test_subtract(calc):
  assert calc.subtract(10, 4) == 6
  
def test_multiply(calc):
  assert calc.multiply(3, 4) == 12


# --- Edge Case Tests ---
def test_divide(calc):
  assert calc.divide(10, 2) == 5.0


def test_divide_by_zero(calc):
  with pytest.raises(ValueError, match="Cannot divide by zero"):
    calc.divide(10, 0)


def test_square_root(calc):
  assert calc.square_root(9) == 3.0


def test_square_root_negative(calc):
   with pytest.raises(ValueError, match="Cannot take square root"):
      calc.square_root(-4)

# def test_add():
#     assert add(2, 3) == 5
#     #assert add(-1, 1) == 0
#     #assert add(0, 0) == 0

# def test_subtract():
#     assert subtract(5, 3) == 2
#     #assert subtract(0, 5) == -5

# def test_multiply():
#     assert multiply(3, 4) == 12
#     #assert multiply(0, 100) == 0
    
# def test_divide():
#     assert divide(10, 2) == 5
#     #assert divide(9, 3) == 3

# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(10, 0)    

# # test_parametrize.py
# @pytest.mark.parametrize('a, b, expected', [
#     (2, 3, 5),
#     (0, 0, 0),
#     (-1, 1, 0),
#     (100, 200, 300),
# ])
# def test_add_parametrized(a, b, expected):
#     assert add(a, b) == expected
        
#To run test_calculator.py ==> pytest in cmd        