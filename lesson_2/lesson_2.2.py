# Урок 2 Задание 2
count = int(input('Enter the number of list items'))
my_list = []
i = 0
n = 0
while i < count:
    my_list.append(input('Enter a new  value for the list '))
    i += 1
for elem in range(int(len(my_list)/2)):
    my_list[n], my_list [n + 1] = my_list[n + 1], my_list[n]
    n +=2
print(my_list)