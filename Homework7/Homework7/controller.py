import interface
import data

def buttons():
    a = interface.actions()
    if a == 1:
        name = interface.get_name()
        number = interface.get_number()
        comment = interface.get_comment()
        
        if len(data.phone_list) == 0:
            max_key = 0
        else:
            max_key = max(data.phone_list.keys())
        
        data.phone_list[max_key+1] = [0,0,0]
        data.phone_list[max_key+1][0] = name
        data.phone_list[max_key+1][1] = number
        data.phone_list[max_key+1][2] = comment

    if a == 2:
        if len(data.phone_list) == 0:
            print('\nСписок пуст.\n')
        else:
            print("id ['Имя','Номер','Комменатрий']")
            for i in data.phone_list:
                print(i,data.phone_list[i])
    if a == 3:
        exit()


