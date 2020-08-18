#Урок 5 Задание 3
import codecs
with codecs.open('lesson_5.3.txt', encoding='utf-8') as my_file:
    salary = []
    low_salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           low_salary.append(i[0])
           salary.append(i[1])

print(f'Оклад меньше 20000 у сотрудников: {low_salary}, средний оклад = {round(sum(map(float, salary)) / len(salary),3)}')

