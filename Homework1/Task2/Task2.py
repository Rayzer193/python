# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import os
os.system('cls')# при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            left = not (x or y or z)
            right = not x and not y and not z
            result = left == right
            if result == True:
                print('[',x,']','[',y,']','[',z,']',"Истина")
            else:
                print('[',x,']','[',y,']','[',z,']',"Ложь")
