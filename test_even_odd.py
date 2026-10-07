from even_odd import evenodd

def test_even():
    assert evenodd(100) == "The Number is Even"

def test_odd():
    assert evenodd(151) == "The Number is Odd"