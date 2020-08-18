#Урок 4 Задание 2
from random import randint
my_list = [randint(1, 300) for i in range(20)]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')