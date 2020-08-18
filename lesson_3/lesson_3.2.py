#Урок 3 Задание 2
name = input('Введите Ваше имя')
surname = input('Введите Вашу фамилию')
year = input('Введите Ваш год рождения')
city = input('Введите Ваш город проживания')
email = input('Введите Вашу электронную почту')
telephone = input('Введите Ваш номер телефона')

def my_func (name, surname,year, city, email,telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print('Ваши данные:',my_func( name , surname , year , city , email , telephone))
