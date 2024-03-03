from myfunc import fib

def test_fib():
    result = fib(4)
    assert result == [0, 1, 1, 2, 3]
