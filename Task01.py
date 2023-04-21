# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

n = int(input("Enter number:  "))
list_1 = list()

for i in range(n):
    x = int(input("Enter digits:  "))
    list_1.append(x)
set1 = set(list_1)
print(set1)

m = int(input("Enter number:  "))
list_2 = list()

for i in range(m):
    y = int(input("Enter digits:  "))
    list_2.append(y)

set2 = set(list_2)
print(set2)

i = set1.intersection(set2)
print(i)


