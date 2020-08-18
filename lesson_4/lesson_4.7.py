#Урок 4 Задание 7

from itertools import count
from math import factorial

f = int(input('Факториал какого числа Вы хотите получить? '))
def factorial_gen():
    for el in count(1):
        yield factorial(el)

gen = factorial_gen()
x = 0
for i in gen:
    if x < f:
        print(i)
        x += 1
    else:
        break
