def mygcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return max(x, y)
print(mygcd(10000000000000000000000000000000000000000000000000000000000000000000, 1))
