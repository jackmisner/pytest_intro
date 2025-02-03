from lib.check_codeword import *

def test_check_codeword():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'
    result = check_codeword('h_anything_else_e')
    assert result == 'Close, but nope.'
    result = check_codeword('not_the_password')
    assert result == 'WRONG!'
