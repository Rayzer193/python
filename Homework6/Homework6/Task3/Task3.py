# Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

list1 = [1, 5, 6, 7, 11, 15, 7]

rast = lambda a,b: a*b

def calc(op,a,b):
    print(op(a,b),end = ' ')
   
print("Произведение пар: ", end ='')
if len(list1)%2 == 0:   
    for i in range(int(len(list1)/2)):
        calc(rast ,list1[i] ,list1[-(i+1)])
else:   
    for i in range(int(len(list1)/2)):
        calc(rast ,list1[i] ,list1[-(i+1)])
    print(list1[int(len(list1)/2)])




