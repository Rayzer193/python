from random import randint
def get_temp(senser):
    return randint(-20,0) if senser else randint(0,20)

def get_press(sensor):
    if sensor:
        return randint(720,750)
    else:
        return randint(750,770)

def get_ws(senser):
    return randint(0,30) if senser == 1 else randint(30,50)

def collection(senser = 1):
    return(get_temp(senser),get_press(senser),get_ws(senser))

