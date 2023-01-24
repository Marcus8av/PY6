#Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random
list_of_numbers = []
for _ in range(10):
    number = random.randint(0, 10)
    list_of_numbers.append(number)
print(list_of_numbers)
print(f'количество различных элементов: {len(set(list_of_numbers))}')