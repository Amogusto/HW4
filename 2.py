from random import randint
my_list = [randint(-100,100) for i in range(10)]
print(my_list)
new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1] and my_list.index(el) != 0]
print(new_list)