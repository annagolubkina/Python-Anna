#Урок 8 задание 4-6
class MyExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt

class Stock:
    names = []

    def __init__(self, name='stock'):
         self.names.append(name)
         self.name = name
         self.storage_number = 0
         self.instorage = {}

    def to_storage(self, stuff): #начальное размещение
        self.storage_number += 1
        stuff.assign_stock_number(self.storage_number)
        stuff.change_department(self.name)
        self.instorage[self.storage_number] = {'type': stuff.type, 'inventory number': stuff.inv_number,
                                               'year': stuff.year, 'model': stuff.model}

    def to_storage_from(self, stuff, from_dep): # перемещение техники
        check = False
        for item in list(from_dep.instorage.values()):
            if stuff.inv_number == item['inventory number']:
                check = True
                break
        if check:
            from_dep.from_storage(stuff)
            self.to_storage(stuff)
        else:
            print(f'В департаменте {from_dep.name} нет техники с инвентаризационным номером {stuff.inv_number}')

    def from_storage(self, stuff): # списание со склада
        self.instorage.pop(stuff.storage_number)
        stuff.assign_stock_number(-1)

    def __str__(self): # результат хранения техники в департаментах
        my_str = f'Сейчас в департаменте {self.name} находятся: \n'
        for key, value in self.instorage.items():
            my_str += f'Складской номер {key}: {value} \n'
        return f" \n {my_str}"


class OfficeEq:
    inv_numbers = []

    def __init__(self, inv_number, year, model):
        try:
            if inv_number in self.inv_numbers:
                self.inv_number = -inv_number
                OfficeEq.append_inv(-inv_number)
                raise MyExceptions('Такой инвентаризационный номер уже существует')
            self.inv_number = inv_number
            OfficeEq.append_inv(inv_number)
            self.model = str(model)
            self.storage = -1
            self.year = int(year)
            if 2020 < year or year < 2010:
                self.year = 2019
                raise MyExceptions(f'Очень старая техника! {year}')

        except ValueError:
            print('Проверьте корректность данных')
        except MyExceptions as err:
            print(err.txt)

    @classmethod
    def append_inv(cls, inv_num): # хранение инвентарных номеров
        OfficeEq.inv_numbers.append(inv_num)

    def assign_stock_number(self, num):
        self.storage_number = num

    def change_department(self, storage):
        self.storage = storage


class Printer(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'printer'
        self.storage = storage
        storage.to_storage(self)  # хранение по умолчанию сразу на складе

class Scanner(OfficeEq):
    def __init__(self, inv_number, year, model, storage, dimension):
        super().__init__(inv_number, year, model)
        self.type = 'scanner'
        self.storage = storage
        self.dimension = dimension
        storage.to_storage(self)

    def to_scan(self):
        return f'to scan page in: {self.dimension} DPI'

class Copier(OfficeEq):
    def __init__(self, inv_number, year, model, storage, num_copy):
        super().__init__(inv_number, year, model)
        self.type = 'copier'
        self.storage = storage
        self.num_copy = num_copy
        storage.to_storage(self)

    def to_copier(self):
        return f'to copier page {self.num_copy} times'



stock = Stock()
it = Stock('IT')
users = Stock('Users')
print(Stock.names)


copier1 = Copier(1919, 2002, 'HP', it, 2)
copier2 = Copier(3245, 2018, 'Canon', stock, 10)
printer1 = Printer(2657, 2012, 'Epson', users)
scanner1 = Scanner(2050,2015, 'HP',it, 400)

it.to_storage_from(copier1, stock)
users.to_storage_from(copier2, stock)
print(stock, it, users)
print(f'Модель первого сканера: {scanner1.model}')
print(f'Год первого ксерокса: {copier1.year}')
print(list(stock.instorage.values()))
print(stock)
print(it)
print(users)
print(scanner1.to_scan())
print(copier2.to_copier())
