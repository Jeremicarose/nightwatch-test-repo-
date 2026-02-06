"""Calculator tests."""
import pytest
import sys
sys.path.insert(0, 'src')

from calculator import add, subtract, multiply, divide, cube

def test_add():
    assert add(2, 3) == 5

def test_cube():
    assert cube(3) == 27

def test_cube_none():
    """FAIL: cube() crashes on None."""
    with pytest.raises(TypeError, match="Cannot cube None"):
        cube(None)


def test_cube_handles_none_input():
    """Verify cube raises TypeError with a specific message when input is None."""
    import pytest
    with pytest.raises(TypeError, match="Cannot cube None"):
        cube(None)
