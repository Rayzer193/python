# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

lst = [1.55, 1.2, 3.1, 5.05, 10.1]
lst_drob = []
for i in range(len(lst)):
    lst_drob.append(lst[i]%1)
print (max(lst_drob)-min(lst_drob))