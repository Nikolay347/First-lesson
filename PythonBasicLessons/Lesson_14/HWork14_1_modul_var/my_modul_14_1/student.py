#my_modul_14_1/student.py

from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        # Initiation by attributes of the class Student object. Instance attributes. Inheritance from human.
        super().__init__(gender, age, first_name, last_name)    # is an override from human
        self.record_book = record_book                          # new definition

    def __str__(self):
        # Defining a custom string representation of an object.
        return super().__str__() + f", {self.record_book}"  # is an override from human + new definition

    def show_info(self):
        print(f"Name: {self.first_name} has {self.record_book}")