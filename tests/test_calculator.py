"""Tests for the calculator module."""

import pytest
import sys
sys.path.insert(0, 'src')

from calculator import add, subtract, multiply, divide, power, square_root


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


def test_divide_handles_zero_divisor():
    """Verify divide raises ValueError when the divisor is zero."""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    """Test basic power functionality."""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1


def test_power_with_none():
    """This test will FAIL - power() doesn't handle None values."""
    result = power(None, 2)
    assert result is None


def test_power_handles_none_base():
    """Verify power returns None when the base is None."""
    result = power(None, 2)
    assert result is None


def test_square_root():
    """Test basic square root functionality."""
    assert square_root(4) == 2.0
    assert square_root(9) == 3.0
    assert square_root(0) == 0.0


def test_square_root_negative():
    """This test will FAIL - square_root() doesn't handle negative numbers."""
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-4)


def test_square_root_handles_negative_input():
    """Verify square_root raises a specific ValueError for negative input."""
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-4)


def test_double():
    """Test doubling numbers."""
    from calculator import double
    assert double(5) == 10
    assert double(0) == 0


def test_double_none():
    """This will FAIL - double() crashes on None."""
    from calculator import double
    with pytest.raises(TypeError, match="Cannot double None"):
        double(None)
