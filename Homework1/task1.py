"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""
n = input('Введите трехзначное число ')
a = int(n[0])
b = int(n[1])
c = int(n[2])
print(a + b + c)

"""
n = int(input('Введите трехзначное число '))
a = n % 10
b = n % 100 // 10
c = n // 100
print(a + b + c)
"""