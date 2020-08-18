#Урок 3 Задание 4
def my_pow(x,y):
    y = abs(y)
    if y == 0:
        return 1
    else:
        return x * my_pow(x, y -1)
x_pow = my_pow(int(input('Введите основание')),int(input('Введите значение степени')))
result = 1 / x_pow
print('Результат=', result)