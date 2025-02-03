from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

def test_multiply_two_nums():
    result = multiply_two_nums(4,6)
    assert result == 24