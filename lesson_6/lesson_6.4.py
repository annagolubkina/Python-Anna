# Урок 6 Задание 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print({self.name},'is going')

    def stop(self):
        print({self.name},'stopped')

    def turn_right(self):
        print({self.name},'is turning right')

    def turn_left(self):
        print({self.name},'is turning left')

    def show_speed(self):
        print('the speed limit for',{self.name}, 'is', {self.speed}, )




class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed limit of {self.name} is higher '
        else:
            return f'Speed limit of {self.name} is normal '


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed limit of {self.name} is higher '
        else:
            return f'Speed limit of {self.name} is normal '

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

BMW = SportCar(120, 'Black', 'BMW 320', False)
Toyota = TownCar(70, 'White', 'Toyota Prius', False)
Citroen = WorkCar(70, 'Grey', 'Citroen ', True)
Skoda = PoliceCar(110, 'Police',  'Scoda', True)
print(BMW.turn_left())
print(Citroen.turn_right())
print(f'When {Citroen.turn_right()}, then {BMW.stop()}')
print(f'{Toyota.go()} with speed exactly {Toyota.show_speed()}')
print(f'{Toyota.name} is {Toyota.color}')
print(f'Is {BMW.name} a police car? {BMW.is_police}')

print(BMW.show_speed())
print(Toyota.show_speed())
print(Skoda.police())
print(Citroen.show_speed())



