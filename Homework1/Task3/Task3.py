# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
import os
os.system('cls')# при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'
print("Введите координату X:",end ='')
x = int(input())
print("Введите координату Y:",end ='')
y = int(input())
if x == 0 and y == 0:
    print("Точка начала координатной плоскости")
if x == 0 and y != 0:
    print("Точка лежит на оси Y")
if y == 0 and x !=0:
    print("Точка лежит на оси X")
if x > 0 and y > 0:
    print("Точка пренадлежит первой четверти")
if x < 0 and y > 0:
    print("Точка пренадлежит второй четверти")
if x < 0 and y < 0:
    print("Точка пренадлежит третей четверти")
if x > 0 and y < 0:
    print("Точка пренадлежит четвертой четверти")