#"Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный
dictionary = []
quantity = 1
for i in range(quantity):
    diction = dict()
    english = input ("Введите слово на английском языке: ")
    russian1 = input ("Введите первый перевод слова: ")
    russian2 = input ("Введите второй перевод слова: ")
    diction[english] = russian1.split (","), russian2.split (",")
    dictionary.append(diction)

print(dictionary)
   