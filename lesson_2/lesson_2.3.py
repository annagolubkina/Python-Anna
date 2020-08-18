# Урок 2 Задание 3
season_dict = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
month = int(input('Choose a month: '))
for key in season_dict.keys():
    if month in season_dict[key]:
        print(key)
    else : print('No matches found in dictionary')
    break

seasons_list = ['winter', 'spring', 'summer', 'autumn']
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[2])
else: print('No matches found in list')
