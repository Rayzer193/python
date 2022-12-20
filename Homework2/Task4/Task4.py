# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

z = float(input("Введите целое число большее нуля: "))
if (z < 0 or z%1 != 0):
    print("Не возможно создать такое множество")
else:
    lst = []
    for i in range((int(z)*(-1)),(int(z)+1)):
        lst.append(i)
    data = open ('file.txt', 'r')
    itog = 1
    for line in data:
        a = int(line)
        if ( a < len(lst)):
            print("Элемент ",a,"=",lst[a])
            itog = itog * lst[a]
    data.close()
    print("Произведение элементов:",itog)
