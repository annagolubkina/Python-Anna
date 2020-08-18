# Урок 8 Задание 2

class OwnError:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return ('Делить на ноль нельзя!')



div = OwnError(10, 200)
print(OwnError.divide_by_null(5, 0))
print(OwnError.divide_by_null(20, 0.1))
print(div.divide_by_null(5000, 0))
