# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

k = int(input('Введите натуральную степень k:'))

kf=[randint(0,100) for i in range(k)]+[randint(1,100)]
ur='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(kf) if j][::-1])

ur=ur.replace('x^1+', 'x+')
ur=ur.replace('x^0', '')
ur+=('','1')[ur[-1]=='+']
ur=(ur, ur[:-2])[ur[-2:]=='^1']

print(ur,"=0",sep = '')