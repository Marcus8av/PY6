#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.
dictionary = []
quantity = int(input('Введите число:'))
for i in range(quantity):
    diction = dict()
    names = input("Введите Имя: ")
    age = int(input("Введите возраст: "))
    diction[names] = age
    dictionary.append(diction)

max_name = " "
ages = 0
for diction in dictionary:
    for name in diction.keys():
        ages += int(diction[name])
        if len(max_name) < len(name):
            max_name = name

age = ages / len(dictionary)
print("Средний возраст среди введенных людей:", int(age))
print("Длинное имя среди введенных л.дей:", max_name)