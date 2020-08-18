# Урок 4 Задание 4
from random import randint
massiv_1 = [randint(1, 20) for i in range(20)]
massiv_2 = [i for i in massiv_1 if massiv_1.count(i) < 2]
print('Исходный массив: ',massiv_1)
print('Итоговый массив:  ', massiv_2)