#The difference between the numbers

def difference(*args: float):
    """
    The program finds the difference between the minimum and maximum arguments among
    the entered array of arguments.
    :param args: unspecified number of arguments as numbers (int, float).
    :return: difference between the minimum and maximum arguments among
    the entered array of arguments.
    :conditions: if there are no arguments, the function returns 0 (zero).
    If the 1 argument is given, then the following is output: "Wrong!
    You input one argument(number)! Need minimum 2 arguments"
    """
    parameters = []             #formation of an iterable list.
    for num in args:
        parameters.append(num)
    if len(parameters)==0:      #The beginning of working out conditions and calculations.
        return print(0)
    elif len(parameters)==1:
        return print("Wrong! You input one argument(number)! Need minimum 2 arguments")
    else:
        max_element = max(parameters)
        min_element = min(parameters)
        diff = round((max_element - min_element), 2)    #Rounding to the second digit, if needed.
        return print("Difference: ", diff)              # Result output.
difference(5, 15)           #Function call.