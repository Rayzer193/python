# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

lst_start = [2, 3, 4, 5, 6, 7, 8]
lst_end = []
if len(lst_start)/2 % 1 > 0:
    l0 = (len(lst_start)/2+1)
else:
    l0 = (len(lst_start)/2)
l = int(l0)
for i in range(l):
    c = (lst_start[i]*lst_start[-(i+1)])
    lst_end.append(c)
print(lst_end)