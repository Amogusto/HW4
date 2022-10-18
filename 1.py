from sys import argv
name, hours, rate, prize = argv
salary = int(hours) * int(rate) + int(prize)
print(salary)