#Урок 4 Задание 6.1
n_1 = int(input('Введите начальное значение списка'))
from itertools import count

for i in count(n_1):
    if i > 20:
        break
    else:
        print(i)

#Урок 4 Задание 6.2
from itertools import cycle

count = 0
for i in cycle('ABC'):
    if count > 9:
        break
    print(i)
    count += 1