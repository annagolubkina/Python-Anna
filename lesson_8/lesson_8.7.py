# Урок 8 Задание 7

class Complex_number:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print('Сумма', {self.a},'и', {self.b}, ' равна:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print('Произведение', {self.a},'и', {self.b}, ' равно:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = Complex_number(5, -7)
z_2 = Complex_number(2, 5)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)