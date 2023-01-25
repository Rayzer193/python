import Sub as model
import interface

def button_click():
    value_a = interface.get_value()
    value_b = interface.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    interface.view(result)