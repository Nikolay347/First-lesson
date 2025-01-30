#A_W# 12.1. Phone book
import csv

import codecs

users = [
    {"name": "Tom", "phone": "+3548943186"},
    {"name": "Nikita", "phone": "+3545543137"},
    {"name": "Alex", "phone": "+3834679228"},
]
action = int(input("Input number action: 1 - (create/addition), 2 - (editing), 3 - (remove), 4 - (search): "))
filename = "phone_book.csv"
if action == 1:
    with open(filename, "a", newline="") as file:
        columns = ["name", "phone"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        # all users
        writer.writerows(users)

        # one user
        # user: dict = {"name": input("Input name: "), "phone": input("Input phone: ")}
        # writer.writerow(user)

        user1: dict = {"name": "Tom", "phone": "+3548943186"}
        user2: dict = {"name": input("Input name: "), "phone": input("Input phone: ")}
        user1 = user2
        writer.writerow(user1)




    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], " - ", row["phone"])


elif action == 2:
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file, )
        contact_ = next(reader)
        print(input("Input name: "), contact_)




        # print(a)
        # for i in a:
        #     if "Tom" in i:
        #         print(i)
