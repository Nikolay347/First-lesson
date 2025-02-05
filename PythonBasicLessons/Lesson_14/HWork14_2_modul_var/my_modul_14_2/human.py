#my_modul_14_1/human.py

class Human:

    def __init__(self, gender, age, first_name, last_name):
        # Initiation by attributes of the class Human object. Instance attributes. No inheritance.
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        # Defining a custom string representation of an object.
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}"

    def show_info(self):
        print(self.__str__())

