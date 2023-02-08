# 1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
#  Последняя строка содержит число X

from random import randint

N = int(input("Введите количество элементов в списке: "))

list = []

for i in range(N):
    list.append(randint(1, 10))
print(list) 

x = int(input("Введите число: "))

count = 0

for i in list:
    if x == i:
        count = count + 1
print(count) 

# Второй вариант

# from random import randint

# N = int(input("Введите количество элементов в списке: "))

# list = []

# for i in range(N):
#     list.append(randint(1, 10))
# print(list)

# x = int(input("Введите число: "))
# print(list.count(x))