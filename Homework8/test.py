import data as DT
import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

print()
otlich = []
itog=[]
k = 0
for key in DT.students:
    for i in range(len(DT.lesons)):
        for j in range(len(DT.students[key][DT.lesons[i]])):
            k = 0
            if DT.students[key][DT.lesons[i]][j] == 1 or DT.students[key][DT.lesons[i]][j] == 2 or DT.students[key][DT.lesons[i]][j] == 3:
                otlich.append(key) 
tpl  = set(otlich)
for key in DT.students:
    if key in tpl:
        True
    else:
        itog.append(key)

for i in range(len(itog)):
    print(itog[i])