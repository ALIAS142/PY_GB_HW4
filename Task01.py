# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств


# Вариант 1
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

# Вариант 2
# var1 = '5 4' # количество элементов первого и второго множества

# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
#
# var2 = set(var2)
# var3 = set(var3)
#
# i = var2.intersection(var3)
# print(i)


# Вариант 3
# n, m = map(int, input().split())
#
# a = set(map(int, input().split()))
#
# b = set(map(int, input().split()))
#
# print(*sorted(a & b))

# Вариант 4
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# list1 = var2.split()
# list2 = var3.split()
# n_set = set(list1)
# m_set = set(list2)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)