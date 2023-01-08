# разыменновывание
def print_dict(**kwargs):
    print(kwargs)


#                key = value
print_dict(a=54, b="hi", key=True)  # {"a": 54, "b": "hi", "key": True}


# ** делает словарь

# task
# написать функцию 
# func(k1=8, k2=6) => вернет сумму значений
# даст 14

def func(**dictionary):
    return sum(dictionary.values())


print(func(k1=8, k2=6))

# .values даст список, мы даем его в sum