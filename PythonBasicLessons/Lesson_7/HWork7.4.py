# Search for common elements
def common_elements():
    import random
    list_3 = []
    # print(type(list_3))
    list_5 = []
    for i in range(0, 100):
        list_3.append(int((random.randrange(0, 1000, 3))))
        list_5.append(int((random.randrange(0, 1000, 5))))
    set3 = {i for i in list_3}
    set5 = {i for i in list_5}


    print(set3)
    print(set5)
    inters = set5.intersection(set3)
    return inters


print("Common elements: ", common_elements())

