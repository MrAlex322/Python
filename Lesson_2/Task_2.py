# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

num = int(input())
a, b = 0, 1
count = 2

while num >= b:
    if b == num:
        print(count)
        break
    a, b = b, a + b
    count += 1
else:
    print(-1)