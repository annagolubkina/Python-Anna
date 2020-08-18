# Урок 7 Задание 2

class Cloth:
    def __init__(self, cloth_v, cloth_h):
        self.cloth_v = cloth_v
        self.cloth_h = cloth_h

    def get_square_coat(self):
        return self.cloth_v / 6.5 + 0.5

    def get_square_jacket(self):
        return self.cloth_h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.cloth_v / 6.5 + 0.5) + (self.cloth_h * 2 + 0.3)}')

class Coat(Cloth):
    def __init__(self,  cloth_v, cloth_h):
        super().__init__(cloth_v, cloth_h)
        self.square_coat = round(self.cloth_v / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat}'


class Jacket(Cloth):
    def __init__(self, cloth_v, cloth_h):
        super().__init__(cloth_v, cloth_h)
        self.square_jacket = round(self.cloth_h * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_jacket}'

my_coat = Coat(2, 4)
my_jacket = Jacket(1, 2)
print(my_coat)
print(my_jacket)
print(my_coat.get_sq_full)
print(my_jacket.get_sq_full)
print(my_jacket.get_square_coat())
print(my_jacket.get_square_jacket())