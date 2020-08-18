#Урок 5 Задание 2

my_file = open('lesson_5.2.txt')
content = my_file.readlines()
print(content)

count = 0
for line in content:
    count +=1
print(f'количество строк в файле - {count}')
c = 0
list_of_lists = []
for line in content:
    c += 1
    line = line.split()
    d = len(line)
    print(f'количество слов в {c} строке - {d}')

