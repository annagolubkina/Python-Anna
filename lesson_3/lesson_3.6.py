# def int_func (*args):
#     word = input("Input words ")
#     print(word.title())
#     return
# int_func()
print('Введите строку')
def int_func(word):

    a_small = word[0]
    a_big = chr(ord(a_small) - ord('a') + ord('A'))
    return a_big + word[1:]

source = input().split()
result = []

for word in source:
    result.append(int_func(word))
print(' '.join(result))