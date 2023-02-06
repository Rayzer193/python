import view

def calculate():
    num_1, num_2, oper = view.get_value()
    match oper:
        case '+': return(num_1 + num_2)
        case '-': return(num_1 - num_2)
        case '*': return(num_1 * num_2)
        case '/': return(num_1 / num_2)

def calculate2(num_1, num_2, oper):
    match oper:
        case '+': return(num_1 + num_2)
        case '-': return(num_1 - num_2)
        case '*': return(num_1 * num_2)
        case '/': return(num_1 / num_2)