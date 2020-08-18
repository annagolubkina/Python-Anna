# Урок 6 Задание 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}



class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname


    def get_total_income(self):
         return self._income.get('wage') + self._income.get('bonus')


a = Position('Иван', 'Иванов', 'Инженер 2 кат.', 50000, 20000)
b = Position('Федор', 'Федоров', 'Начальник лаборатории', 100000, 50000)

print(a.get_full_name(), a.position, a.get_total_income())
print(b.get_full_name(), b.position, b.get_total_income())
