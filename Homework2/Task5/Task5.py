# Реализуйте алгоритм перемешивания списка

import os
import random 
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'
lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(lister) 
print(lister)