#Урок 5 Задание 4

russian = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('lesson_5.4.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(russian[i[0]] + '  ' + i[1])

with open('lesson_5.4_new.txt', 'w') as my_file_2:
    my_file_2.writelines(new_file)
    print('Новый файл успешно записан!')