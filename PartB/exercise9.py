factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Test cases
print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(5))
print(factorial(10))
