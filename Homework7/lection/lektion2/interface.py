import start_data as dat
import log

def temp_view(sensor):
    data = dat.get_temp(sensor)
    log.temp_log(data) 
    return data

def press_view(sensor):
    data = dat.get_press(sensor)
    log.press_log(data) 
    return data

def ws_view(sensor):
    data = dat.get_ws(sensor)
    log.ws_log(data) 
    return data
