# Add 1 to number

def add_one(*args):
    a = list(*args)
    res = int(''.join(str(i) for i in a))
    b = res + 1
    k = []
    for i in str(b):
        k.append(int(i))
    print(k)
add_one([9])



