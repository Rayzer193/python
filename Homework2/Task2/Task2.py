# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

n = int(input("введите число: "))
z = 1
print('[', end = '')
for i in range(n-1):
    z = z * (i+1)
    i += 1
    print(z,end = ',')
z = z * n
print(z,']', sep = '')