"""Tests for the calculator module."""

import pytest
import sys
sys.path.insert(0, 'src')

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero():
    """This test will FAIL because divide() doesn't handle zero division."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_divide_raises_value_error_on_zero_divisor():
    """Verify divide raises ValueError with a specific message when divisor is zero.

    This test will fail with the current implementation because it raises
    ZeroDivisionError instead of ValueError. It will pass once the fix
    is applied to raise ValueError for zero division.
    """
    with pytest.raises
