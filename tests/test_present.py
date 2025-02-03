import pytest
from lib.present import *
present = Present()

def test_wrap():
    result = present.wrap('test_present')
    assert result == None

    with pytest.raises(Exception) as e:
        present.wrap('second_present')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap():
    result = present.unwrap()
    assert result == 'test_present'

    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
