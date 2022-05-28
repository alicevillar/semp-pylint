
SOME_GLOBAL_VAR = 'GLOBAL VAR NAMES SHOULD BE IN ALL_CAPS_WITH_UNDERSCOES'

def multiply(variable_x, variable_y):
    result = variable_x* variable_y
    if result == 777:
        print("jackpot!")
    return result

def is_sum_lucky(variable_x, variable_y):
    """This returns a string describing whether or not the sum of input is lucky
    This function first makes sure the inputs are valid and then calculates the
    sum. Then, it will determine a message to return based on whether or not
    that sum should be considered "lucky"
    """
    if variable_x is not None:
        if variable_y is not None:
            result = variable_x+variable_y
            if result == 7:
                return 'a lucky number!'

        return 'just a normal number'


class SomeClass():
    """"
    Classe para xxxx
    """
    def __init__(self, some_arg,  some_other_arg):
        self.some_other_arg = some_other_arg
        self.some_arg = some_arg
