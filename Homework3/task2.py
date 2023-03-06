"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

import random 

#N = int(input('Введите количество элементов в массиве: '))

#lst = [random.randrange(10) for _ in range(N)]
#print(lst)

#new_lst = list(map(int, lst))

#X = int(input('Введите число Х: '))

#count = 0
#n = 0

#for i in range(N):
#    if (X - lst[i]) <= X - n and X - lst[i] >= 0:
#    n = i
#    count += 1

#print(lst[n])

N = int(input('Введите количество элементов в массиве: '))
lst = [random.randrange(10) for _ in range(N)]
print(lst)

X = int(input('Введите число Х: '))

n = abs(X - lst[0])  # abs() - модуль числа
index = 0
for i in range(N):
    count = abs(X - lst[i])
    if count < n:
        n = count
        index = i

print(lst[index])