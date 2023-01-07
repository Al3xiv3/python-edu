def factorial(n):
    if n <= 0:
        return None
    if n == 1:  # база
        return 1
    return n * factorial(n - 1)

print(factorial(5))
