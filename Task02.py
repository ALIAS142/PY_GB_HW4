# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Enter number:  "))
list1 = list()

for i in range(n):
    x = int(input("Enter digits:  "))
    list1.append(x)

print(list1)

Maxres = 0
i = 1
for i in range(1, n-1):
    if (list1[i] + list1[i + 1] + list1[i - 1] > Maxres):
     Maxres = list1[i] + list1[i + 1] + list1[i - 1]
print(Maxres)


# while i <= len(list_1):
#               resultMax = result
#               result = (len(list_1[0]) + len(list_1[1]) + len(list_1[2])
#               (list_1[0]) += 1
#
#               result == resultMax
#
#               print(resultMax)
