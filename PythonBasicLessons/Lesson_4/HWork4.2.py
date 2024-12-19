lst = []
new_lst1 = []
if bool(lst) == False:
    print(lst, ' => ', 0)
else:
    for i in lst:
        if lst.index(i) % 2 == 0:
            new_lst1.append(i)
    new_lst2 = sum(new_lst1) * lst[-1]
    print(lst, ' => ',  new_lst2)
