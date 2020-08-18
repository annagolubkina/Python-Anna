# #Урок 5 Задание 6
# import codecs
#
# dict = {}
# with open('lesson_5.6.txt', encoding='utf-8') as my_file:
#     for line in my_file:
#         subject, lect_s, prac_s, lab_s = line.split()
#
#         lecture = str(lect_s)
#         if lecture == '-':
#             lecture = 0
#         else:
#             lecture= int(lect_s)
#
#         practice = str(prac_s)
#         if practice == '-':
#             practice = 0
#         else:
#             practice = int(prac_s)
#
#         labaratory = str(lab_s)
#
#         if labaratory == '-':
#             labaratory = 0
#         else:
#             labaratory = int(lab_s)
#
#         dict[subject] = int(lecture) + int(practice) + int(labaratory)
#     print(f'Общее количество часов по предмету - \n {dict}')
#
import random
lst = []
for _ in range(10):
    lst.append(random.randint(-10,10))
print(lst)