# Урок 6 Задание 2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

class CountBitumen(Road):
    def __init__(self, _length, _width, volume, thick):
        super().__init__(_length, _width)
        self.volume = volume
        self.thick = thick

    def mass(self):
        return self._length * self._width *self.thick * self.volume


count = CountBitumen(20, 5000, 25, 5)
print(f' Масса асфальта - ' f'{count.mass()/1000}', 'т.')



