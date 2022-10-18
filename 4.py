from random import randrange
my_list = [randrange(0,20) for i in range(40)]
new_list = [i for i in my_list if my_list.count(i) < 2]
print(new_list)