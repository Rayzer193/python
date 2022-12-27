# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

print("Введите числа через пробел:")
a = [int(i) for i in input().split()]
for i in range(len(a)):
   f = 1
   for j in range(len(a)):
      if a[i] == a[j] and i != j:
         f = 0
         break
   if f:
      print(a[i], end = ' ')