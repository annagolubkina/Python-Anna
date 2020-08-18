# Урок 2 Задание 4
words = list(map(str,input('Input sentence ').split()))
for c, value in enumerate(words, 1):
    print(c, value [:10])
