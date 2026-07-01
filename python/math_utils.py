# math_utils.py - Mathematical and Statistical utility functions
def mean(numbers):
  if len(numbers) == 0:
    raise ValueError("mean() requires at least one number")
  return sum(numbers) / len(numbers)

def maximum(numbers): return max(numbers)

def minimum(numbers): return min(numbers)

def range_of(numbers):
  if len(numbers) == 0:
    raise ValueError("numbers must not be empty")
  current_min = current_max = numbers[0]
  for num in numbers[1:]:
    if num < current_min:
      current_min = num
    if num > current_max:
      current_max = num
  return current_max - current_min

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
