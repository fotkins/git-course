# ctrl + D - дублировать строку

# name_of_person = 'Anastasia'
# print(name_of_person[-1]) - выводит последнюю букву с конца
# print(name_of_person[0:5]) - выводит срез первых букв, 5 не вк
# print(name_of_person[:5]) - от начала до 5
# print(name_of_person[2:]) # - от второго включительно до конца
# print(name_of_person[0:8:2]) - выводит символы в диапазоне от 0 до 8 с шагом 2 (каждый второй)
# print(name_of_person[10::-1]) - выводит в обратном порядке
# print(name_of_person[::-1]) - тоже выводит в обратном порядке
# print(name_of_person[::-1], name_of_person[:])

# email = 'welcome@mail.ru
# index = email.find('@')
# print(index) - находим порядковый номер символа (7)
# print(email[:index]) - выводим все символы до index (т.е. '@') не включая
# name = 'ПеТрОв иВаНоВ'
# print(name.lower()) - выводит все буквы маленькими
# print(name.upper()) - выводит все буквы заглавными
# print(name.capitalize()) - выводит первую букву заглавную, отсальные прописными
# print(name.title()) - Выводит каждое слово после пробела с большой буквы
# print(len(name)) - кол-во символов в строке
# print(name.count('о')) - считает сколько раз встречается буква
# print(name.split()) - разделение на слова в лист через запятую ['ПеТрОв', 'иВаНоВ']
# print(name.split('р')) #- разделение на слова с разделителем ['ПеТ', 'Ов иВаНоВ']
# _________________________________________________
# name = 'Ivan'
# age = 30
# money = 200.2
#
# # print('Hello', name, 'вам', age, 'лет', 'у вас', money)
#
# # result = 'Hello %s вам %i лет, у вас %f' %(name, age, money)
# # result = 'Hello {} вам {} лет, у вас {}'.format(name, age, money)
# result = f'Hello {name} вам {age} лет, у вас {money}!' # самый современный способ f string
# print(result)
# ______________________________

# name = 'Sergey'
# humans = ['Ivan', 'Alex', 'Olga', name]
# print(humans[::-1])
# humans[0] = 'Nastya'

# humans.append(10) - добавляет 10 в конец листа
# humans.insert(1, 200) вставляет на позицию 1 элемент 200
# print(humans.index(name))
# humans.remove('Ivan') - удаляет элемент Ivan конкретный
# humans.remove(humans[1]) - удаляет элемент листа на позиции 1
# deleted_element = humans.pop(0)
# print(humans)
# print(deleted_element)
# ____________
# x = [1, 2, 3, ['qwe', 'asd']]
# print(x[3][0]) - обращение к вложенному элементу - выводит qwe

# ____________ for in (список или кортеж) - перебор значений
# humans = ['Ivan', 'Alex', 'Olga']
# for name in humans:
#     print(name)
# for i in "qwerty":
#     print(i, "Hi!")
# ____________

# a = x = 00
# my_list = []
#
# while x < 100:
#     my_list.append(x)
#     x += 10
# print(*my_list, sep=' ')
# y = [i+1 for i in my_list]
#
# print(*y, sep=' ')


# numbers = [1, 2, 3]
# my_list = []
# for name in numbers:
#     my_list.append(name)
# print(my_list)

# Даны списки:

# for i in range(1, 10):
#     print(i, "hello")
# _________выводим определенное кол-во раз hello______________


# -------------------- С Л О В А Р И -----------------------
# human = {'name': 'Alex', 'age': 43, 'money': 39.1}
# human['data'] = [1, 2, 3, 3] добавляем ключ со значением в словарь
# print(human['age']) получаем содержимое словаря по ключу
# print(human.get('name')) проверяем существует ли ключ и выводим если да
# human['input'] = input() добавляем ключ в словарь, значение вводит пользователь
# .pop([1]) - удаляет элемент по указанному индексу и возвращает его. Если индекс не указан, то удаляет и возвращает последний элемент.
# для словаря нужно указать ключ
# .popitem() - удаляет элемент с конца - Python 3.8+

# for key in human.keys():
#     print(key)
# for value in human.values():
#     print(value)
# for key, value in human.items():
#     print(key + ":", value)
# -------------------- С Л О В А Р И -----------------------

# ------------------- М Н О Ж Е С Т В А --------------------
# my_set = {1, 1, 2, 2, 2, 3, 3, 3, 6}
# print(len(my_set))

# a = {1, 2, 3, 8}
# b = {3, 4, 5}
# print(a | b)
# - Объединение множеств
# print(a & b) - пересечение {3}
# print(a - b)
# print(a ^ b) - все кроме пересечений
