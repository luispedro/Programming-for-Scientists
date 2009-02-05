from stddev import stddev

def test_constant():
    assert stddev([1]*20) < 1e-3
def test_positive():
    assert stddev(range(2)) > 0
