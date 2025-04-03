def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return a ** 0.5
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def fibonacci(n):
    if n < 0:
        raise ValueError("Cannot compute Fibonacci of negative number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def prime_factors(n):
    if n <= 1:
        raise ValueError("Cannot compute prime factors of number less than or equal to 1")
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_even(n):
    return n % 2 == 0
def is_odd(n):
    return n % 2 != 0
def lcm_of_list(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    lcm_result = numbers[0]
    for number in numbers[1:]:
        lcm_result = lcm(lcm_result, number)
    return lcm_result
def gcd_of_list(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    gcd_result = numbers[0]
    for number in numbers[1:]:
        gcd_result = gcd(gcd_result, number)
    return gcd_result
def mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)
def median(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
def mode(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_frequency]
    return modes
def variance(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    mean_value = mean(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
def standard_deviation(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return variance(numbers) ** 0.5
def permutations(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result
def combinations(lst, r):
    if r == 0:
        return [[]]
    if len(lst) < r:
        return []
    result = []
    for i in range(len(lst)):
        rest = lst[i+1:]
        for c in combinations(rest, r - 1):
            result.append([lst[i]] + c)
    return result
