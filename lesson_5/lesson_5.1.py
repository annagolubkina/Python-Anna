#Урок 5 Задание 1

my_file = open('lesson_5.1.txt', 'w')

line = input('Введите текст \n')

while line:
    my_file.writelines(line + '\n')
    line = input('Введите текст \n')
    if not line:
        break
my_file.close()

my_file = open('lesson_5.1.txt', 'r')
text = my_file.readlines()
print(f'Результат записи: {text}')
my_file.close()
