# Урок 6 Задание

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки',{self.title})


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('У вас в руках', self.title, 'Запуск отрисовки ручкой')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('У вас в руках', self.title, 'Запуск отрисовки карандашом')



class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('У вас в руках', self.title, 'Запуск отрисовки маркером')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())