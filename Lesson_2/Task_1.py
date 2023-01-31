# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

num = int(input())
count = 1
all_pow = 1

while num >= count:
    all_pow *= count
    count += 1

print(all_pow)