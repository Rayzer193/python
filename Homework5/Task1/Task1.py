#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

del_combination = 'абв'
print("Введите строку слов:")
str1 = str(input())
str2 = list(filter(lambda rmv: del_combination not in rmv.lower(), str1.split()))
print(*str2)
