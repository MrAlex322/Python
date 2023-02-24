# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list=[]
for i in range(10):
    list.append(randint(1,20))
print(list)

min = int(input("Введите минимальную границу: "))
max = int(input("Введите максимальную границу: "))

for i in list:
    if i > min and i < max:
        print(i)

