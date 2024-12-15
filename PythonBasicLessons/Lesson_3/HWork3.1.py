num1 = int(input("Input 1 number: "))
num2 = int(input("Input 2 number: "))
Action = input("Input one of action (+ - * /) :  ")
act = ['+', '-', '*', '/']

if Action in act:
    if Action == "+":
        print("Result is: ", num1+num2)
    elif Action == "-":
        print("Result is: ", num1 - num2)
    elif Action == "*":
        print("Result is: ", num1 * num2)
    elif Action == "/":
        if num2 != 0:
            print ("The divisor isn`t equal to zero!")
            print("Result is: ", num1 / num2)
        else: print("Error! Division by zero! Input correct operation!")
else:
    print("Not correction input date! Repeat, please!")

#Для більш профі калькуляторів напевно потрібно використання методів виключень))
