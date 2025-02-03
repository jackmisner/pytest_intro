from lib.string_builder import *

def test_string_size():
    sb = StringBuilder()
    sb.add("first_string")
    result = sb.size()
    assert result == 12

def test_output():
    sb = StringBuilder()
    sb.add("first_string")
    result = sb.output()
    assert result == "first_string"
    sb.add(", ")
    sb.add("second_string")
    result = sb.output()
    assert result == "first_string, second_string"
