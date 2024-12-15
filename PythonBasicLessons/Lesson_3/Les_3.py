# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки
#
# print("hello" in "hello world")

# print(bool(0))
# False
# print(bool(1))
# True
# print(bool(None))
# False

####
# ввести з клавіатури 3 числа
# - вивести найменше із трьох чисел
# - кiлькiсть однакових чисел

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))

# - вивести найменше із трьох чисел #???
# v1
# if number2 < number1 < number3 or number2 < number3 < number1:
#     print(number2)
# elif number3 < number1 < number2 or number3 < number2 < number1:
#     print(number3)
# elif number1 < number3 < number2 or number1 < number2 < number3:
#     print(number1)

# print('var2')
#
# if number1 == number2 == number3:  # number1 == number2 and number2 == number3
#     print("All numbers are equal")
# else:
#     if number1 <= number2:
#         if number1 < number3:
#             print(number1)
#         else:
#             print(number3)
#     elif number2 <= number3:
#         if number2 < number1:
#             print(number2)
#         else:
#             print(number1)
#     elif number3 <= number1:
#         if number3 < number2:
#             print(number3)
#         else:
#             print(number2)

###
# user_select = int(input("1. Start\n2. Settings\n3. Saved games\n4. Exit\nSelect your choice: "))
#
# # v1
# if user_select == 1:
#     print("Starting game...")
# elif user_select == 2:
#     print("Settings")
# elif user_select == 3:
#     print("Saved games")
# elif user_select == 4:
#     print("Exit")
# else:
#     print("Invalid input please try again")
#
# # # v2
# match user_select:
#     case 1:
#         print("Starting game...")
#     case 2:
#         print("Settings")
#     case 3:
#         print("Saved games")
#     case 4:
#         print("Exit")
#     case _: # аналог else
#         print("Invalid input please try again")

###
# b=None
# a=5
# if bool(b):
# 	c = b
# else:
# 	c = a
# print(c)
###Difficult logic expressions (сложні логічні вирази)!!!!!!!!
# a=int(input('Input number: '))
# if a<0:
#     a=""
# s1=a
# s2="world"
# print(s1>s2)
#
# print(s1 and s2)
# print(s1 or s2)
# #
# a= int(input("Input number: "))
# if a>45:
#     print("Wait plz!");
#     print("The condition is accepted")
# else:
#     print("Not right! Try again!")
###
# c = input("Input stroke: ")
# print("The stroke is consist of: ", len(c), " symbols")
# if 0 < len(c) < 10:
#     print("Warning!")
# elif len(c) >= 10:
#     print("Normal input learning number symbols!")
# else:
#     print("Re-enter!")

###
# print(type([1, 3, 5]))
# print(type(list()))
# print(list("Hello world!!!"))

#
# lst_lst = [
#     [9, 12, 3], # <- 0
#     [4, 5, 46]  # <- 1
# ]
# print(lst_lst[0]) # Перший "рядок" [9, 12, 3]
# print(lst_lst[1]) # Другий "рядок" [4, 5, 46]
#
# first_list = [2, 4, 7, 11, 0, -2, 8]
# first_list.insert(5, 40)
#
# print(first_list)  # [2, 4, 7, 11, 0, 40, -2, 8]
#
#
# lst = [3, 1, 4, 1, 5, 9, 1, 2, 6, 5]
# lst.remove(1) # видаляє перше входження 1 зі списку
# lst.remove(1)
# lst.remove(11)
# print(lst) # [3, 4, 1, 5, 9, 2, 6, 5]
##
# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# x = lst.pop(2) # повертає значення 4 і видаляє його зі списку
# print(x) # 4
# print(lst) # [3, 1, 1, 5, 9, 2, 6, 5]

##
# lst = (3,5,8,2,7)
# k = 5
# if k in lst:
#     print("Element", k, "in in the list!")

##
# lst = [3, 5, 7]
# lst.extend([8, 4, 56])
# print(lst) # [3, 5, 7, 8, 4, 56]
# lst2 = [3, 5, 7]
# lst2.append([8, 4, 56])
# print(lst2) # [3, 5, 7, [8, 4, 56]]

##############################################################################
## Тема "Збільшення списку на ціле число". При розкритті теми зауважується про
# обережність при створенні нового списку, коли, в якості елементів
# використовується тип даних, що змінюється! Що саме мається на увазі?
# Розумію так, що, якщо треба робити новий список, то він не повинен робитися
# зі старого. Бо це означатиме ідентифікацію нового списка по адресу старого.
# І це, можливо зітре адресу старого. Тобто він "пропаде".
# Але ж, створивши новий список з новим ім'ям, але задавши тіж самі значення
# елементів -- нова id -адреса новому списку не присвоїлась!
# .
##
l = [[]] * 3
print(l)            # вивелось [[], [], []]

# Всі три елементи новоствореного списку - це один і той же список
print(id(l[0]))     # вивелась id адреса: 2004656836864
print(id(l[1]))     # вивелась id адреса: 2004656836864
print(id(l[2]))     # вивелась id адреса: 2004656836864

print()

first_list = [2, 4, 7]
my_list = first_list * 3

print(my_list)              # вивелось [2, 4, 7, 2, 4, 7, 2, 4, 7]
print(id(first_list[0]))    # вивелась id адреса: 140712147536344
print(id(my_list[0]))       # вивелась id адреса: 140712147536344
# А тепер з новим списком і тими ж елементами по значенню:
my=[2, 4, 7, 2]
print(id(my[0]))            # вивелась id адреса: 140712147536344
#
print(id(my[3]))            # вивелась id адреса: 140712147536344
#Відмічається, що одне і теж саме значення елементу має одну і
# ту ж саму id-адресу, без різниці де б цей елемент не стояв.


# Тобто, що саме мається на увазі: "Висновок - не можна використовувати
# такий підхід при створенні нового списку, коли в якості елементів
# використовується тип даних, що змінюється"?
# /Прошу вибачення за питання, можливо не на те звертаю увагу, не туди
# "копаю"!)

#
first_list = [2, 4, 7, 11, 0, -2, 8]

print(first_list[5: 2: -1])  # [-2, 0, 11]
print(first_list[6: 3: -1])  # [8, -2, 0]
dig = [1,2,3,4,5,6,7,8,9,10,11,12]
print(dig[9:7:-1])     #[10,9]
print(dig[10:6:-1])     #[11,10,9,8]