#Урок 5 Задание 5
from random import randint

my_list = [randint(1, 100) for i in range(10)]
new_list = [str(i) +' ' for i in my_list]
with open('lesson_5.5.txt', 'w') as f:
        f.writelines(new_list)
print(sum(map(int,new_list)))