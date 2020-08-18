#Урок 4 Задание 5
from functools import reduce
def multi (el_1, el):
    return el_1 * el
print(f'Список четных значений от 100 до 1000- {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения элементов  - {reduce(multi, [el for el in range(99, 1001) if el % 2 == 0])}')

# def my_func(el_p, el):
#     return el_p * el
#
# print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
# print(f'Результат перемножения элементов  {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')