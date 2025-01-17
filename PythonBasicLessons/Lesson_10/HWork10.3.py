#Checking whether a number is even
def is_even(digit):
    """
    Checking whether a number is even
    :param digit: input date. Integer number.
    :return: raising number to the power.
    :conditions:True if the number is even, and False if the number is not even.
    :output date: logical type.
    """
    if digit % 2 == 0:
        return True
    else:
        return False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
