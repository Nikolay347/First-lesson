# Generator function
#Final version for homework 10.1:
# # 2**1 = 2
# # 2**2 = 4          основа 2 в ступені 2 дорівнює результату 4
# # 2**4 = 16
# # 2**8 = 256
# Тобто бачимо виконання результату при незмінності за кожен крок основи, і змінності ступеня з
# кроком (*2) за кожен крок. Це досягається за рахунок застосування ф-ціі my_pow при повторних ітераціях,
# при яких функція my_pow приймає в якості аргументу попередній результат.

def my_pow(x):
    """
    The function raises a number to a power. User function.
    :param x: basis of number (int).
    :param power: power of number (int).
    :return: raising number to the power.
    :conditions: Function with two parameters only - x and power!
    """
    return x ** 2


def some_gen(begin, n_elem, func):              #
    """
        The generator function (using the yield operator) that will return one term
    of a numerical sequence, the law of which is specified using the user function
    :param begin: given the value of the first term of the progression (int).
    :param n_elem: the number of members issued to the sequence (int).
    :param func: parameter represented by user function, that raises a number to a power.
    :return: given generated numeric sequence.
    :conditions: the parameters of the generator function should be the value
     of the first term of the progression and the number of terms given to the
     sequence. The generator must stop its work upon reaching the n-th term.
    """
    current = begin                              # Introduce a variable for the possibility of iterations
    for i in range(n_elem):
        yield current
        current = func(current)                  # Insert a function into the loop by assigning it to a variable

from inspect import isgenerator                  # Modul calling for generators verification. Return true if the
                                                 # is a generator.

gen = some_gen(2, 4, my_pow)        # Function calling
print(gen)
print(list(gen), "==", [2, 4, 16, 256])
gen = some_gen(2, 4, my_pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')



# #Draft version #1 (with the modified user function):
# def my_pow(x, power):
#     """
#     The function raises a number to a power. User function.
#     :param x: basis of number (int).
#     :param power: power of number (int).
#     :return: raising number to the power.
#     :conditions: Function with two parameters only - x and power!
#     """
#     return x ** power
#
# def some_gen(begin, n_elem, func):              #
#     """
#         The generator function (using the yield operator) that will return one term
#     of a numerical sequence, the law of which is specified using the user function
#     :param begin: given the value of the first term of the progression (int).
#     :param n_elem: the number of members issued to the sequence (int).
#     :param func: parameter represented by user function, that raises a number to a power.
#     :return: given generated numeric sequence.
#     :conditions: the parameters of the generator function should be the value
#      of the first term of the progression and the number of terms given to the
#      sequence. The generator must stop its work upon reaching the n-th term.
#     """
#     counter = 0                                 # counter to ensure the given numbers of n_elem.
#     power = 1                                   # iterates degree
#     while counter != n_elem:                    # cycle
#         yield func(begin,power)                 # operator yield
#         counter += 1                            # iterates counter
#         power *= 2                              # iterates degree ("stupin"'))
#
# from inspect import isgenerator                  # Modul calling for generators verification. Return true if the object is a generator.
# gen = some_gen(2, 4, my_pow)        # Function calling
#
# #print(list(gen), "==", [2, 4, 16, 256])        # Interesting!!!, that if "on" - Test#2, without calling the function again, is don't work!
# #gen = some_gen(2, 4, my_pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')
#
# # print(type(gen))
# # print(gen)
#
# #####################################################################################
# #Draft version #2 (code version with question! Not for passing the task. For error discussing.): As a result,
# we get a generated list within list(or three lists, may be variant). As a result, Test 2 was not passed!
# Perhaps the code should be complicated by methods of opening lists (perhaps decomposition methods)?
# #
# # def my_pow(x):
# #     return x ** 2
# #
# # def some_gen(begin, n_elem, func):
# #     k = [begin]
# #     while len(k) != n_elem:
# #         k.append(func(k[-1]))
# #     yield k
# #     # print(k)
# #
# # gen = some_gen(2, 4, my_pow)
# # print(type(gen))
# # print(list(gen))
# # print(gen)
# #
# #
# # from inspect import isgenerator
# # gen = some_gen(2, 4, my_pow)
# #
# # assert isgenerator(gen) == True, 'Test1'
# # assert list(gen) == [2, 4, 16, 256], 'Test2'
# # print('OK')
# #################################################################################################################
