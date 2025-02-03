from lib.report_length import *

def test_report_length():
    result = report_length("four")
    assert result == 'This string was 4 characters long.'
    result = report_length('test_sentence')
    assert result == 'This string was 13 characters long.'