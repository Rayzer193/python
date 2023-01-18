# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

def primer_list (primer):
    prim_list  =  {}
    primer = primer.replace(' - ',' -').replace(" + ",' +')
    primer = primer.split(' ')
    primer = primer[:-2]
    for i in range(len(primer)):
        primer[i] = primer[i].replace('+','').split("x**")
        prim_list[int(primer[i][1])] = int(primer[i][0])
    return prim_list

def  list_summ(list1,list2):
    final_list ={}
    max_sep = (max(max(list1),max(list2)))
    for i in range(max_sep,-1,-1):
        num1 = list1.get(i)
        num2 = list2.get(i)
        if num1 != None or num2 != None:
            final_list[i] = (num1 if num1 != None else 0) + (num2 if num2 != None else 0)
    return final_list

def primer_result(itog):
    result = ""
    for i in itog.items():
        if result == "":
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
    result = result.replace('x^1','x').replace('x^0','').replace('1x^','x^') + ' = 0'
    return result

with open("input1.txt", 'r') as text:
    primer1 = text.readline()
with open("input2.txt", 'r') as text:
    primer2 = text.readline()

prim_list1 = primer_list(primer1)
prim_list2 = primer_list(primer2)
itog_list = list_summ(prim_list1,prim_list2)
vyvod = primer_result(itog_list)

with open("output.txt", 'w') as text:
    text.writelines(vyvod)