#The program is designed and suitable for all examples given in the homework...

###
slist = []
number = len(slist)
if number%2 != 0:
    list1 = slist[:(number + 1)//2]
    list2 = slist[(number+2)//2:]
else:
    list1 = slist[:number//2]
    list2 = slist[number//2:]
print(list1)
print(list2)
result1 = [list1, list2]
print(result1)
print()

##
slist2 = [1, 2, 3, 4]
number2 = len(slist2)
if number2%2 != 0:
    list12 = slist2[:(number2 + 1)//2]
    list22 = slist2[(number2+2)//2:]
else:
    list12 = slist2[:number2//2]
    list22 = slist2[number2//2:]
print(list12)
print(list22)
result2 = [list12, list22]
print(result2)
print()

##
slist3 = [1, 2, 3]
number3 = len(slist3)
if number3%2 != 0:
    list13 = slist3[:(number3 + 1)//2]
    list23 = slist3[(number3+2)//2:]
else:
    list13 = slist3[:number3//2]
    list23 = slist3[number3//2:]
print(list13)
print(list23)
result3 = [list13, list23]
print(result3)
