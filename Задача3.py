#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Найдите самого младшего из друзей и выведите его имя.
dictionary = {}
quantity = int(input('Введите число:'))
for i in range(quantity):
    name = input("Введите Имя: ")
    age = int(input("Введите возраст: "))
    dictionary[name] = age

min_value = min(dictionary.values())
for name, am in dictionary.items():
    if am == min_value:
        print(name)