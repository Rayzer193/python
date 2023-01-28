import interface as UI
import data as DT
import generator as GEN

def buttons():
    print()
    a = UI.actions()
    if a == 1:          #1.Добавить студента.
        print()
        name = UI.get_name()
        sename = UI.get_sename()
        new_key = name + ' ' + sename
        DT.students.update({new_key:{}})
        for i in range (len(DT.lesons)):
            lesson1 = DT.lesons[i]
            DT.students[new_key].update({lesson1:[]})

    if a == 2:          #2.Добавить предмет.
        print()
        print('Доступные предметы: ',*DT.lesons)
        print('Добавить предмет\n', end = '')
        lesson2 = UI.get_lesson()
        DT.lesons.append(lesson2)
        for key in DT.students:
            DT.students[key].update({lesson2:[]})

        print('Доступные предметы: ',*DT.lesons)
  
    if a == 3:         #3.Добавить оценку.
        print()
        print('Список учеников:')
        for key in DT.students:
            print(key)
        name3 = UI.get_name()
        print('Введите предмет по которому хотите увидеть оценки')
        print('Список Предметов:')
        for i in range(len(DT.lesons)):
            print(DT.lesons[i])
        lesson3 = UI.get_lesson()
        print('Прдемет:', lesson3)
        grad = UI.get_grade()
        while grad <1 or grad>5:
            print("Неверный ввод, оценка может быть от 1 до 5")
            grad = UI.get_grade()
        DT.students[name3][lesson3].append(grad)

    if a == 4:          #4.Показать список учеников
        print()
        for key in DT.students:
            print(key)

    if a == 5:          #5.Показать оценки ученика
        print()
        print('Введите имя ученика по которому хотите увидеть оценки')
        print('Список учеников:')
        for key in DT.students:
            print(key)
        name5 = UI.get_name()
        print()
        print('Введите предмет по которому хотите увидеть оценки')
        print('Список Предметов:')
        for i in range(len(DT.lesons)):
            print(DT.lesons[i])
        lesson5 = UI.get_lesson()
        print('Ученик',name5,'по предмету',lesson5,'имеет следующие оценки:', *DT.students[name5][lesson5])

    if a == 6:          #6.Сгенерировать 100 сулчайных учеников
        GEN.generate()
    
    if a == 7:          #7.средний бал ученика по предмету
        print()
        print('Введите имя ученика по которому хотите увидеть оценки')
        print('Список учеников:')
        for key in DT.students:
            print(key)
        name7 = UI.get_name()
        print()
        print('Введите предмет по которому хотите увидеть оценки')
        print('Список Предметов:')
        for i in range(len(DT.lesons)):
            print(DT.lesons[i])
        lesson7 = UI.get_lesson()
        l = sum(DT.students[name7][lesson7])/len(DT.students[name7][lesson7])
        print('Средняя оценка ученика',name7,'по предмету',lesson7,'является',l )
    
    if a == 8:      #8.среднего балла по школе по конкретному предмету
        print()
        print('Введите предмет по которому хотите увидеть  среднюю оценку оценки')
        print('Список Предметов:')
        for i in range(len(DT.lesons)):
            print(DT.lesons[i])
        lesson8 = UI.get_lesson()
        l = 0
        for key in DT.students:
            l += sum(DT.students[key][lesson8])/len(DT.students[key][lesson8])
        l = l/len(DT.students)
        print('Средняя оценка школы по предмету',lesson8,'является',l )

    if a == 9:      #9.вывод отличников
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

        print('Всего оличников',len(itog),':')
        for i in range(len(itog)):
            print(itog[i])

    if a == 0:
        exit()
    
    if a == 625:        #тест для просмотра нынешнего списка
        print(DT.students)