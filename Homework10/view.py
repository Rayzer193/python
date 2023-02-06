import interface as IN

def view_data(data, title):
    title = (f'{IN.num_1} {IN.oper} {IN.num_2}')
    print(f'{title} = {data}')

def get_value():
    return IN.inp2()