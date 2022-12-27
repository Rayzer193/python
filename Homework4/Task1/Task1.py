# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

d = int(input("Введите точность:"))
k = 1
x = 0
for k in range(1, 1000000):
    x = x+4*((-1)**(k+1))/(2*k-1)
template = '{:.' + str(d) + 'f}'
print(template.format(x))