number = int(input("Input a four-integer number: "))
num1 = number//1000
num2 = number%1000//100
num3 = number//10%10
num4 = number%10

print(num1, end='\n\n')
print(num2, end='\n\n')
print(num3, end='\n\n')
print(num4, end='\n\n')
