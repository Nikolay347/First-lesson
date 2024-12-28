import string
import copy

number = input("Input some number: ")

while int(number) > 9:
    num = str(number)   #str
    number = 1
    for elem in num:
        number*=int(elem)
print("->", number)






# num = num.expandtabs(0)
