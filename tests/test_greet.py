from lib.greet import *

def test_greet():
    result = greet("Jack")
    assert result == "Hello, Jack" 