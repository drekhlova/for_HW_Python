"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""

n = int(input('Введите кол-во элементов первого множества: '))
n1 = (input('Введите через пробел элементы первого множества: ')).split()

m = int(input('Введите кол-во элементов второго множества: '))
m1 = (input('Введите через пробел элементы второго множества ')).split()

print(n1)
print(m1)

arr = n1 + m1

print(sorted(''.join(set(arr))))