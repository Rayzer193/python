#Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, 
# игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в 
# виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает 
# соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим
# поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик 
# в ряд по диагонали, вертикали, горизонтали)
import os

# начальное поле
field = [1,2,3,4,5,6,7,8,9]
 
# условия победы
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 
# вывод поля
def print_field():
    print('',field[0], ' |',field[1],' |',field[2], '\n', field[3], ' |',field[4],' |',field[5],'\n',field[6], ' |',field[7],' |',field[8])

# ход в ячейку указанного номера
def step_field(step, symbol):
    ind = field.index(step)
    field[ind] = symbol
 
# итог игры
def checkwin():
    win = ''

    for i in wins:
        if field[i[0]] == '✕' and field[i[1]] == '✕' and field[i[2]] == '✕':
            win = '✕'
        if field[i[0]] == '◯' and field[i[1]] == '◯' and field[i[2]] == '◯':
            win = '◯'   
    return win
 
# поиск линии бота с ✕ и ◯ на победных линиях
def check_line(sum_O, sum_X):
 
    step = ''
    for line in wins:
        o = 0
        x = 0
 
        for j in range(0,3):
            if field[line[j]] == '◯':
                o = o + 1
            if field[line[j]] == '✕':
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if field[line[j]] != '◯' and field[line[j]] != '✕':
                    step = field[line[j]]
    return step
 
# выбор хода бота
def bot_move():        
 
    step = ''
 
    # 2 свои и 0 чужих
    step = check_line(2, 0)
 
    # 2 чужих и 0 своих
    if step == '':
        step = check_line(0, 2)        
 
    # 1 своих и 0 чужих
    if step == '':
        step = check_line(1, 0)           
 
    # занять центр если пуст
    if step == '':
        if field[4] != '✕' and field[4] != '◯':
            step = 5           
 
    # занять первую если центр не пуст
    if step == '':
        if field[0] != '✕' and field[0] != '◯':
            step = 1           

    return step
 
def main():
    game_over = False
    player = True
    
    while game_over == False:
    
        # показываем поле
        os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'
        print_field()
    
        # ход игрока
        if player == True:
            symbol = '✕'
            step = int(input('Ваш ход(укажите номер ячейки куда поставить ✕ ):'))
        else:
            # ход бота
            print('Бот сделал свой ход: ')
            symbol = '◯'
            step = bot_move()
    
        if step != '':
            step_field(step, symbol)
            # определение победителя
            win = checkwin()
            if win != '':
                game_over = True
            else:
                game_over = False
        else:
            game_over = True
            win = 'Ничья'
    
        player = not(player)        
    
    # игра окончена, вывод результатов
    os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'
    print_field()
    if win == 'Ничья':
        print('Ничья')
    else:
        print('Победил Бот' if win=='◯' else 'Вы победили')

if __name__ == '__main__':
    main()