import pytest
from operations import add, subtract, multiply, divide, InvalidOperationError

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 4) == -8

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(InvalidOperationError):
        divide(1, 0)