#Найдите сумму цифр трехзначного числа.
num = int(input("Введите трехзначное число: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print ("Сумма чисел равно: ", sum)