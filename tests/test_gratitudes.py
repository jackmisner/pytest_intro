from lib.gratitudes import *

gratitudes = Gratitudes()

def test_add():
    result = gratitudes.add('Health')
    assert result == None

def test_formatted():
    result = gratitudes.format()
    assert result == 'Be grateful for: Health'
    gratitudes.add('Happiness')
    result = gratitudes.format()
    assert result == 'Be grateful for: Health, Happiness'