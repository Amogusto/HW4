from random import randrange
from functools import reduce
def mult(prev, el):
    return prev * el

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
print(reduce(mult, my_list))