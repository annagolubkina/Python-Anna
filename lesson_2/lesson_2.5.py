# Урок 2 Задание 5
my_list = [7,5,3,3,2]
count = int(input('Enter a new  value for the list'))
for elem in range(int(len(my_list)/2)):
        if my_list[elem] == count:
            my_list.insert(elem + 1, count)
            break
        elif my_list[0] < count:
            my_list.insert(0,count)
        elif my_list[-1] > count:
            my_list.append(count)
        elif my_list[elem] > count and my_list[elem + 1] < count:
            my_list.insert(elem + 1, count)
print(my_list)
