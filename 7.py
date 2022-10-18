def fact(n):
    prev = 1
    for el in range(1, n):
        factorial = prev * el
        prev = factorial
        yield factorial

my_list = [el for el in fact(10)]
print(my_list)