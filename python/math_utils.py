# math_utils.py - Mathematical and Statistical utility functions
def mean(numbers):
  return sum(numbers) / len(numbers)

def maximum(numbers): return max(numbers)

def minimum(numbers): return min(numbers)

def range_of(numbers):
  return max(numbers) - min(numbers)

def add(a, b): return a + b

def multiply(a, b): return a * b

def is_even(n): return n % 2 == 0

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
