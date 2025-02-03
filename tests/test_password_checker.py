import pytest
from lib.password_checker import *

pc = PasswordChecker()

def test_password_length():
    with pytest.raises(Exception) as e:
       pc.check('123456')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    result = pc.check("123456789")
    assert result == True