# For revision was used the calc from homework #3.1.
while True:
    action_1 = input("Input calculation ('y') or something to stop calculation: ")
    if action_1 == "y":
        action_2 = input("Input one of action (+ - * /):  ")
        num1 = int(input("Input 1 number: "))
        num2 = int(input("Input 2 number: "))

        act = ['+', '-', '*', '/']

        if action_2 in act:
            if action_2 == "+":
                print("Result is: ", num1+num2)
            elif action_2 == "-":
                print("Result is: ", num1 - num2)
            elif action_2 == "*":
                print("Result is: ", num1 * num2)
            elif action_2 == "/":
                if num2 != 0:
                    print ("The divisor isn`t equal to zero!")
                    print("Result is: ", num1 / num2)
                else: print("Error! Division by zero! Input correct operation!")
        else:
            print("Not correction input date! Repeat, please!")
    else:
        print("Stop calculation command!")
        break
