from mymathlib import add, subtract, multiply, divide, power, square_root, factorial, gcd, lcm, fibonacci, prime_factors, is_prime, is_even, is_odd

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 3) == 2
def test_multiply():
    assert multiply(3, 2) == 6
def test_divide():
    assert divide(6, 3) == 2
    try:
        divide(1, 0)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for division by zero"
def test_power():
    assert power(2, 3) == 8
def test_square_root():
    assert square_root(9) == 3
    try:
        square_root(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for square root of negative number"
def test_factorial():
    assert factorial(5) == 120
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for factorial of negative number"
