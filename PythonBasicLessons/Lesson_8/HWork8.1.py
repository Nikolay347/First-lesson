# Add 1 to number

def add_one(number):
    # a = list(number) # assigning a variable to the parameter(list)
    numb = int(''.join(str(i) for i in list(number)))   #convert to int format
    b = numb + 1    #adding 1 according to the condition of the task
    k = []  #formation of the final list
    for i in str(b):
        k.append(int(i))
    print(k)
add_one([5,6,8,7])      #function calling



