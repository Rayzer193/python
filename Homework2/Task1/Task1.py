# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

num = input("Введите число: ")
x = num.split(".") 
if (len(x) == 2):
    x = num.split(".") 
    a = int(x[0])
    b = int(x[1])
    mult = 0
    if (a!=0):
        while (a != 0):
            mult = mult + (a % 10)
            a = a // 10
    if (b!=0):
        while (b != 0):
            mult = mult + (b % 10)
            b = b // 10
else:
    a = int(num)
    mult = 0
    while (a != 0):
        mult = mult + (a % 10)
        a = a // 10
print("Произведение цифр равно:", mult)