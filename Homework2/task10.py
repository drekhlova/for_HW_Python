"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""
##n = int(input('Введите количество монеток: '))

##a = 0
##b = 0

##for i in range(n):
##    x = int(input())
##    if x == 0:
##        a += 1
##    else:
##        b += 1
##if b > a:
##    print(a)
##else:
##    print(b)

"""
n = int(input('Введите количество монеток, лежащих на столе: '))
count = 0
i = 0
while i < 0:
    type = int(input('Орел или решка\n:'))
    if type != 1 and type != 0:
        print('Недопустимое значение')
        continue
    elif type == 1:
        count += 1
        i += 1
    else:
        i +=1
if n - count == 0 or count == 0:
    print('Ничего переворачивать не нужно')
elif count == n - count:
    print(f'Одинаковое количество орлов и решек, по {count} штук. Можно переворачивать любые.')
else:
    print(f'Минимальное количество {count}. Этих орлов надо перевернуть и будет {n} решек.')
"""

from random import randint
coins = [randint(0 , 1) for _ in range(int(input()))]
print(coins)
print(min(
    coins.count(0),
    coins.count(1)
))
