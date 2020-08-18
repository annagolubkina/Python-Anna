#Урок 3 Задание 5
def my_sum():
    sum_result = 0
    a = False
    while a == False:
        number = input('Введите числа или нажмите Q для выхода ').split()

        result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                a = True
                break
            else:
                result = result + int(number[el])
        sum_result = sum_result + result
        print(f'Текущая сумма = {sum_result}')
    print(f'Окончательная сумма =  {sum_result}')

my_sum()

