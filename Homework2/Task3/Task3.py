# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

n = int(input("Введите число:"))
lst = []
for i in range(1, n+1):
    elem = round((1+1/i)**i, 3)
    lst.append(elem)
print("Последовательность: {", end = '')
for j in range(len(lst)-1):
    print (j+1,': ',lst[j],sep = '',end = ', ')
print (n,': ', lst[-1],'}',sep = '')
print('Сумма:' ,'{:.2f}'.format(sum(lst)))
