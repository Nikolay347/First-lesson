import string

ht = list((input("Input date for hashtag: ")).title())

for i in ht[:]:
    if i in string.punctuation or i == " ":
        ht.remove(i)
ht = ''.join(ht)
ht1 = f"#{ht}"

if len(ht1) > 140:
    ht1 = ht1[:140]

print("->", ht1)
print("Hashtag initial length", len(f"#{ht}"))
print("Hashtag result length", len(ht1))