#Урок 3 Задание 3
def my_func(arg_1,arg_2,arg_3):
    list_1 = sorted([arg_1, arg_2, arg_3])
    list_1.pop(0)
    sum = 0
    for i in list_1:
        sum += i
    return sum
print(f'Результат - {my_func(int(input("Введите первое значение ")), int(input("Введите второе значение  ")), int(input("Введите третье значение  ")))}')

