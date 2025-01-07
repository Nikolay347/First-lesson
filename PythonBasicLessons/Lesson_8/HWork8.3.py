#Unic number
def find_unique_value(*args):
    for i in sp:
        cnt = sp.count(i)
        if cnt == 1:
            print(i)
            break
sp = [5, 5, 5, 2, 2, 0.5]

find_unique_value(sp)
