from myfunc import fib, fib_nth

def test_fib():
    result = fib(4)
    assert result == [0, 1, 1, 2, 3]

def test_fib_nth():
    assert fib_nth(6) == 6
