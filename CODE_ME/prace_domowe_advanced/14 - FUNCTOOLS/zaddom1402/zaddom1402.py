# Rafał Nitychoruk
from adv_border import add_advanced_border
from functools import reduce

def string(a, b):
    return add_advanced_border(a, b, 5, 1)

result = reduce(string, ['Dzień\nDobry', 'a', 'b', 'c', 'd', 'e'])

print(result)
