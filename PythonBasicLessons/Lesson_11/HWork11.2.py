#11.2. Filling the list with cubes of numbers
##################################################################################################
# var.1:
def generate_cube_numbers(end):
    """
    generator function generate_cube_numbers that generates a list of number cubes
    :param end: determined final value, (class 'int')
    :return: list of number cubes (class 'generator')
    :conditions: the formation of sets of cubes of numbers should start from the
    number 2 to the value you specify. The generator must run until a value less
    than the specified value is generated. Output from the generator is possible
    using return without parameters
    """
    for i in range(2, end):
        if i**3 <= end:
            yield i**3

    return

print(list(generate_cube_numbers(100)))
# print(type((generate_cube_numbers(100))))

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("Ok")

########################################################################################################
# var.2:
# def generate_cube_numbers(end):
#     x = 2
#     while True:
#         num_list = x**3
#         if num_list > end:
#             break
#         yield num_list
#         x += 1
#     return
# print(list(generate_cube_numbers(100)))
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print("Ok")