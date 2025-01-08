# Add 1 to number

def add_one(number):
    numb = int(''.join(str(i) for i in list(number)))   #convert to int format
    numb_1 = numb + 1    #adding 1 according to the condition of the task
    new_numb = []  #formation of the final list
    for i in str(numb_1):
        new_numb.append(int(i))
    print(new_numb)

add_one([5,6,8,7])          #function calling



