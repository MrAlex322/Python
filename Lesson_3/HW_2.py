# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

N = int(input("Введите количество элементов в списке: "))

list = []

for i in range(N):
    list.append(i)
list.sort()
print(list)


x = int(input("Введите число: "))

if x in list:
    print(list[(list.index(x) - 1)]) 
else:
    print(list[N-1])

