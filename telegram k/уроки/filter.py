a = [0, 20, 23, 1512, 2333, 122, 893, 211, 122]

'''
def f (x):
    if x > 100:
        return True
    else:
        return False

b = list(filter(f, a))

print(b)

'''

def f (x):
    return x > 100

b = list(filter(f, a))

print(b)

c = list(filter(lambda x: x > 150, a))

print(c)

z = '12ed1d11231s1s11lf12e1k1'

v = list(filter(str.isdigit, z))

print(v)


d = {
    "math": 4,
    "inf": 3,
    "eng": 3,
    "phys": 5,
    "litr": 5,
}

lst = list(filter(lambda x: d[x] > 4, d))

print(lst)
