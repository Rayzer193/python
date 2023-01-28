import random as r
import data as DT
# import interface as UI

men_names = ['Александр','Леонид','Аркадий','Иван','Евгений','Константин','Артемий','Лев','Тимофей','Артём']
women_names = ['Алия','Ярослава','Ольга','Светлана','Амина','Ксения','Виктория','Елизавета','Алина','Варвара']
men_senames = ['Кузьмин','Рудаков','Жаров','Кононов','Савицкий','Алексеев','Носков','Филиппов','Морозов','Никифоров']
women_senames = ['Кузьмина','Рудакова','Жарова','Кононова','Савицкийа','Алексеева','Носкова','Филиппова','Морозова','Никифорова']
lesons_base = ['Русский', 'Математика','Физика','Информатика']

def generate():   
    for i in range(len(lesons_base)):
        DT.lesons.append(lesons_base[i])
    
    for i in range(90):     #генерация 90 случайных учеников

        male = r.randint(1,2)       #генерация пола ученика

        if male == 1:       #генерация мальчика
            name = men_names[r.randint(1,10)-1]
            sename = men_senames[r.randint(1,10)-1]
            new_key = name + ' ' + sename
            DT.students.update({new_key:{}})
            for i in range (len(lesons_base)):
                lesson = lesons_base[i]
                DT.students[new_key].update({lesson:[]})
                for i in range(5):
                    DT.students[new_key][lesson].append(r.randint(1,5))

        if male == 2:       #генерация девочки
            name = women_names[r.randint(1,10)-1]
            sename = women_senames[r.randint(1,10)-1]
            new_key = name + ' ' + sename
            DT.students.update({new_key:{}})
            for i in range (len(lesons_base)):
                lesson = lesons_base[i]
                DT.students[new_key].update({lesson:[]})
                for i in range(5):
                    DT.students[new_key][lesson].append(r.randint(1,5))
    
    for i in range(10):     #генерация 10 случайных отличников

        male = r.randint(1,2)#генерация пола ученика

        if male == 1:#генерация мальчика
            name = men_names[r.randint(1,10)-1]
            sename = men_senames[r.randint(1,10)-1]
            new_key = name + ' ' + sename
            DT.students.update({new_key:{}})
            for i in range (len(lesons_base)):
                lesson = lesons_base[i]
                DT.students[new_key].update({lesson:[]})
                for i in range(5):
                    DT.students[new_key][lesson].append(r.randint(4,5))

        if male == 2:#генерация девочки
            name = women_names[r.randint(1,10)-1]
            sename = women_senames[r.randint(1,10)-1]
            new_key = name + ' ' + sename
            DT.students.update({new_key:{}})
            for i in range (len(lesons_base)):
                lesson = lesons_base[i]
                DT.students[new_key].update({lesson:[]})
                for i in range(5):
                    DT.students[new_key][lesson].append(r.randint(4,5))
