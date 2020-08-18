# Урок 8 Задание 3

class Error_list:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Вводите значение и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Список на данный момент - {self.my_list} \n ')
            except:
                print('Недопустимое значение - строка и булево')
                y_or_n = input(f'Попробовать еще раз? Y/Q ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'Q' or y_or_n == 'q':
                    return 'Осуществлен выход'
                else:
                    return 'Осуществлен выход'

try_except = Error_list(1)
print(try_except.my_input())