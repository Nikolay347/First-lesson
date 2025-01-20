# Parity check
#Var.#1:
def is_even(number):
    """
    Parity check
    :param number: input date. Integer number.
    :return: logical type.
    :conditions: Don't allow use division in functions and actions associated with it.
    That is, it is forbidden to use /, //, % and divmod.
    """
    end_num = str(number)[-1]
    num_ends_for_not_even = (0, 1, 3, 5, 7, 9)
    if int(end_num) in num_ends_for_not_even:
        print(False)
        return False
    else:
        print(True)
        return True

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
#################################################################################################################

#Var.#2:

# def is_even(number):
#     if not number & 1:                  # Found on the Internet as Lorentz invariance and covariance.
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
