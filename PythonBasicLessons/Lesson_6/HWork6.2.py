# Date converter
num = int(input("Input time from 0 to 8640000,s: "))

day = []
hour = []
min = []
sec = []

if bool(num//86400):day = [num//86400]
else:day = [00]

if bool(num%86400//3600):hour = [num%86400//3600]
else:hour = [00]

if bool(num%86400%3600//60):min = [num%86400%3600//60]
else:min = [00]

if bool(num%86400%3600%60):sec = [num%86400%3600%60]
else:sec = [00]

print(f"Result date: {day}days_{hour}hours_{min}minutes_{sec}seconds")

