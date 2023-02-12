# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств

from random import randint

list_1 = [int(input()) for _ in range(int(input("Ведите количество элементов первого списка: ")))]
list_1.sort()
list_2 = [int(input()) for _ in range(int(input("Ведите количество элементов второго списка: ")))]
list_2.sort()
print(list_1)
print(list_2)

1
for i in list_1: 
    for j in list_2: 
        if i == j:
            print (i, end=" ")

# вариант 2

# list_1 = [int(input()) for _ in range(int(input("Ведите количество элементов первого списка: ")))]
# list_2 = [int(input()) for _ in range(int(input("Ведите количество элементов второго списка: ")))]

# print(list_1)
# print(list_2)

# set_1 = set()

# for i in list_1: 
#     for j in list_2: 
#         if i == j:
#             set_1.add(i)
# print(*set_1)

# вариант 3. через сет

# set_1 = {int(input()) for _ in range(int(input("Ведите количество элементов первого списка: ")))}
# set_2 = {int(input()) for _ in range(int(input("Ведите количество элементов второго списка: ")))}
# print(set_1 & set_2)