from datetime import datetime as dt
def temp_log(data):
    time = dt.now().strftime('%h:%M')
    with open('log.csv','a') as file:
        file.write('{};temp;{}\n'
                    .format(time, data))

def press_log(data):
    time = dt.now().strftime('%h:%M')
    with open('log.csv','a') as file:
        file.write('{};press;{}\n'
                    .format(time, data))


def ws_log(data):
    time = dt.now().strftime('%h:%M')
    with open('log.csv','a') as file:
        file.write('{};ws;{}\n'
                    .format(time, data))
