from keyword import kwlist
# import string
#rdok = input("Input variable: ")
rdok = "assert_exception"


var1 = 0
for i in rdok:
    if i in list("!”#$%&'()*+,-./:;<=>?@[\]^`{|}~"):
        var1+=1
if "_" in rdok and len(rdok) == 1:
    print(True)
    # print("_")
elif "__" in rdok or "___" in rdok  or " " in rdok or rdok in kwlist:
    print(False)
    # print("Інфо по відповіді: Не відповідає умові 3 або 5.")
elif not rdok.islower() or bool(var1) or rdok[0].isdigit():
    print(False)
    # print("Інфо по відповіді: Не відповідає умові 2 або 4 або 6.")
else:
    print(True)
    #print("Умова! Змінна не повинна:\n1.Починатися з цифри.\n2.Містити великі літери.\n3.Містити пробіл, або декілька (2 або 3) нижні підкреслення, введені підряд.\n4.Містити знаки пунктуації, окрім нижнього підкреслення'_'.\n5.Бути жодним із зареєстрованих слів.\n6. Починатися з цифри.")
