#Задание 1
a_1 = input('Введите ваше имя:')
a_2 = int(input('Введите год Вашего рождения:'))
year = 2020
print('Здравствуйте', a_1)
if (year - a_2) % 5 == 0:
    print('У Вас юбилей в этом году!')
else:
    print('Вам',(year - a_2), 'лет')

#Задание 2
sec = int(input('Введите количество секунд:'))
import datetime
t = datetime.timedelta(seconds = sec)
datetime.timedelta(0, 65)
str(t)
print(t)

#Задание 3
n = int(input('Введите число:'))
n_new = str(n)
n_1=int(n_new*2)
n_2 =int(n_new*3)
result = n + n_1 +n_2
print(result)

#Задание 4
c = int(input('Введите число:'))
r = -1
while c != 0:
    d = c % 10
    b //= 10
    if d > r:
        r = d
print(r)

#Задание 5
receipt = int(input('Введите значение Вашей выручки'))
cost = int(input('Введите значение Ваших издержек'))
if receipt > cost:
    profit = ((receipt - cost) / receipt) * 100
    profit = round(profit, 2)
    print('Ваша фирма отработала с прибылью,','рентабельность составляет =',profit, '%')
else:
    print('Ваша фирма отработала в убыток')
count = int(input('Введите количество сотрудников'))
eff = round(receipt / count, 2)
print('Прибыль в расчете на одного сотрудника составляет = ', eff)

#Задание 6
a = int(input('Результат в первый день, км:'))
b = int(input('Общий результат, км:'))
i = 1
while a < b:
    a = a + a * 0.1
    i = i + 1
print('На', i, 'день спорстсмен достиг результата не менее', b, 'км')
