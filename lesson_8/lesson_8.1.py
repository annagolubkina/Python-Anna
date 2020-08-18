# Урок 8 Задание 1

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        new_date = []

        for i in day_month_year.split():
            if i != '-': new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def valid_number(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Все введно верно'
                else:
                    return f'Неправильный формат ввода года '
            else:
                return f'Неправильный формат ввода месяца'
        else:
            return f'Неправильный формат ввода дня'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('14 - 06 - 2020')
print(today)
print(Data.valid_number(11, 11, 2022))
print(today.valid_number(11, 13, 2011))
print(Data.extract('15 - 11 - 2019'))
print(today.extract('17 - 04 - 1991'))
print(Data.valid_number(12, 12, 1812))
