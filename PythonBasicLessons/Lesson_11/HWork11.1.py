# 11.1. Generator of prime numbers
def prime_generator(end):           #outer function
    """
    The generator function prime_generator returns prime numbers from
    the range, the upper limit of which is determined by the parameter
    of this function.
    :param end: upper value of range (clas 'int')
    :return: list of number cubes (class 'generator')
    """
    def is_prime(number):           #inner function for determine the type
                                    # of number - simple or complex. Returns
                                    # a Boolean value (status) of True or False
        status = True
        for count in range(2, end+1):
            if number % count == 0 and number != count and count != 1:
                status = False
            # return status
        return status               # end of inner function.
    for i in range(2, end+1):
        if is_prime(i):             # calling an inner function
            # print(is_prime(i))
            yield i
    return

print((list(prime_generator(15))))

from inspect import isgenerator

gen = prime_generator(29)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
###############################################################################################
