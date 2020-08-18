#Урок 4 Задание 1
from sys import argv
def my_salary():
    try:
        time = float(input('Введите количество отработанного времени в часах'))
        salary = int(input('Введите значение ставки в y.e'))
        bonus = int(input('Введите значение премии в у.е. '))
        result = time * salary + bonus
        print(f'заработная плата сотрудника  {result}')
    except ValueError:
        return print('Ошибка!Не число')
my_salary()
