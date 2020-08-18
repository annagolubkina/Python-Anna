#Урок 3 Задание 1
def my_division (*args):

    try:
     arg_1 = int(input('Ввведите первое число'))
     arg_2 = int(input('Ввведите второе число'))
     result = arg_1 / arg_2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "Ошибка!Исключено деление на 0!"

    if arg_2 != 0:
        return arg_1 / arg_2
    else:
        print("Wrong number! Devider can't be null")

print(f'результат:  {my_division()}')
