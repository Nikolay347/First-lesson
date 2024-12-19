import random
lst = []
for i in range(random.randint(3, 10)):
    lst.append(random.randint(0, 1000))
# lst = [1, 1, 2, 1]                  # For manual testing
print(lst)
new_lst = [0,0,0]

new_lst[0] = lst[0]
new_lst[1] = lst[2]
new_lst[2] = lst[-2]
print(new_lst)

