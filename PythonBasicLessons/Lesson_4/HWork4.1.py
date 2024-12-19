spisok  = [1, 0, 13, 0, 0, 0, 5]
print(spisok)
for i in spisok:
    if i ==0:
        spisok.remove(0)
        spisok.append(0)
print(spisok)