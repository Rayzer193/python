# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

x1, y1, x2, y2 = int(input("Введите координату X первой точки: ")), int(input("Введите координату Y первой точки: ")), int(input("Введите координату X второй точки: ")), int(input("Введите координату Y первой точки: "))

rast = lambda a,b,c,d: (((c-a)**2)+((d-b)**2))**0.5

def calc(op,xa,ya,xb,yb):
    print(round(op(xa,ya,xb,yb),3))
   
print("Растояние междуточками: ", end ='')
calc(rast ,x1 ,y1 ,x2 ,y2)
