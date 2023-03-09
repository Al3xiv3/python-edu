def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = list(map(int, numbers))
    return f'{max(numbers)} {min(numbers)}'

print(high_and_low('1 2 3 4 5'))