# print('Hellow world!', 10)
# Ctrl + / - комментирровать

# a = 100
# b = 20
# print(a % b) - остаток от деления
# print(a ** b) - возведение в степень
# print (a // b) - целочисленное деление

# типы данных:

# a = 10
# b = 222.1
# c = 'yes'
# is_admin = True # False # bool
# people = [10, 50, a, 'no'] # список / list
# peoples = (10, 50, a, 'no') # tuple / кортеж
# people.append(30) - метод добавляет к списку еще один элемент, кортеж не позволяет добавлять элементы

# human = {'name': 'Ivan', 'age': 30, 'data': is_admin} # dict / словарь
# print(type(human))
# print (human)

# a = 100
# b = '1'
#
# # print(a + int(b)) - изменение типа данных на число (int)
# # print(str(a) + b) - изменение типа данных на строку (str)
# d = 100.2
# c = int(str(a) + b) * 2 + d

# print(c)

# name = input('Your name: ')
# print('Hello,' , name) - input всегда тип данных - str

# age = int(input('Your age: '))
# print('Your age', age + 10)
# print(5 > 1)
# print(5 > 1)
# print(5 == 1) равно ли? - False - не равно
# print(5 != 1) а не равно ли? - True - да, не равно
# print(5 >= 1) True
# print(5 <= 1) False
# print(bool(0)) - False
# print(bool('')) - False - bool всегда не равен нулю / пустоте

# price = 100
# money = int(input('We have money: '))
# if money >= price:
#     print('yes')
# elif price - money <= 5:
#     print('we can trade')
# else:
#     print('no')

# name = input('Name:')
# ensure = input('Surname:')
# if name and surname:
#     print('You have inputted name and surname')
# elif name or ensure:
#     print('You have imputed ONLY name and surname')
# else:
#     print('Nothing have been inputted')
# ____________________CYCLE_________________
# number = int(input('Insert number from 1 to 5:'))
#
# while number < 1 or number > 5:
#     print('Error, try again')
#     number = int(input('Insert number from 1 to 5:'))
# else:
#     print('Well done')
# _______________________CYCLE____________________

# x = 0
# while x < 10:
#     print(x)
# x += 1 то же самое x = x+ 1  - инкремент

# x = 0
# while x <= 10:
#
#     x += 1
#     if x == 8:
#         print('закончили')
#         break
#
#     elif x == 4:
#         continue
#     print(x)
#
# x = 0
# while x < 10:
#     print(x)
#     x += 1
# else:
#     print('Cycle is over')
# ____________

#     __________ PIN CODE _________________

# pin = int(input('Insert your pin code: '))
# x = 0
#
# while pin != 7755:
#     x += 1
#     print('try again')
#     pin = int(input('Insert your pin code: '))
#
#     if x > 1:
#         print('access blocked')
#         break
# else:
#     print('Welcome!')
#     print(x +3 ** 3)
# _______________PIN CODE OVER______________________

# x = int(input('Insert X: '))
# y = int(input('Insert Y: '))

# x = x - y # 10 - 2 = 8
# y =
# print('X =', x)
# print('Y =', y)
# ______COOL TASK____________

# x = int(input('Insert X: '))
# y = int(input('Insert Y: '))
#
# x = x + y
# y = x - y
# x = x - y
#
# print('X =', x)
# print('Y =', y)
#
# ______________COOL TASK END________________

# __________HARD TASK______________
name = str(input('Insert your name: '))
surname = str(input('Insert your surname: '))
age = int(input('Insert your age: '))
weight = int(input('Insert your weight: '))

# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

if age < 30 and 50 < weight < 120:
    print(name, surname, 'Your age: ', age, 'Your weight: ', weight)
    print('All good')
elif age > 30 and (weight < 50 or weight > 120):
    print(name, surname, 'Your age: ', age, 'Your weight: ', weight)
    print('Need attention')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, surname, 'Your age: ', age, 'Your weight: ', weight)
    print('Need help')
else:
    print('Insert correct information')