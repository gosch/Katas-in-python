

def outter_function(parameter):
    def inner_function(internal_parameter):
        return internal_parameter[parameter]**2.0
    return inner_function

func_list = [outter_function(i) for i in range(5)]

x = list(range(0, 50, 10))
for i in func_list:
    print(i(x))
