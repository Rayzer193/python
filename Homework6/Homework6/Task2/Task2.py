# Найти сумму чисел списка стоящих на нечетной позиции

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

list = [1, 5, 6, 7, 9, 11, 15, 7]
list = [list[i] for i in range(len(list)) if i %2 ]
print (sum(list))