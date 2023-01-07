def factorial(n):
  if n <= 0:
    return None
  x = 1
  for i in range(2, n + 1):
    x = x * i
  return x

print(factorial(5)) # 120
print(factorial(-5)) # None
