import pytest
import sys
sys.path.insert(0, 'src')
from calculator import add, decrement

def test_add():
    assert add(2, 3) == 5

def test_decrement():
    assert decrement(5) == 4

def test_decrement_none():
    with pytest.raises(TypeError, match="Cannot decrement None"):
        decrement(None)


def test_decrement_handles_none_type_error_regression():
    """Verify decrement raises TypeError with the specific 'unsupported operand' message when n is None."""
    with pytest.raises(TypeError, match="unsupported operand type\\(s\\) for -: 'NoneType' and 'int'"):
        decrement(None)
