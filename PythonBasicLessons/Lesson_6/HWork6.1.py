import string


let = (input("Enter letter#1 and letter#2 through the dash: "))

print(let)
let_1 = let[0]
let_2 = let[2]

ver_1 = str(string.ascii_letters.find(let_1))
ver_2 = str(string.ascii_letters.find(let_2))
spisk = str(string.ascii_letters)

print(spisk[int(ver_1):int(ver_2)+1])




