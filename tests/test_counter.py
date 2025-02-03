from lib.counter import *

def test_counter_report():
    counter = Counter()
    counter.add(1)
    counter.add(2)
    counter.add(3)
    counter.add(4)
    result = counter.report()
    assert result == 'Counted to 10 so far.'