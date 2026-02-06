import pytest
import sys
sys.path.insert(0, 'src')
from calculator import add, double

def test_add():
    assert add(2, 3) == 5

def test_double():
    assert double(5) == 10

def test_double_none():
    with pytest.raises(TypeError, match="Cannot double None"):
        double(None)
