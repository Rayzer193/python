# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

k = int(input('Введите число:'))

lst1 = [0,1]
for i in range(2,k+1):
    lst1.append(lst1[i-1] + lst1[i-2]) 

k = -k
k=-(k-1)

lst2 = [1,0]
for j in range(2,k+1):
    lst2.append(lst2[j-2] - lst2[j-1]) 
lst2.remove(0)
lst2.remove(1)  
lst2.reverse()

print(lst2 + lst1)