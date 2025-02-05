#my_modul_14_1/student.py

from human import Human
# from group import Group


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        # Initiation by attributes of the class Student object. Instance attributes. Inheritance from human.
        super().__init__(gender, age, first_name, last_name)    # is an override from human
        self.record_book = record_book                          # new definition



    def __str__(self):
        # Defining a custom string representation of an object.
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}, {self.record_book}"
        # return super().__str__() + f", {self.record_book}"  # is an override from human + new definition

    def show_info(self):
        print(f"Name: {self.first_name} has {self.record_book}")

    def find_student(last_name):
        for student in Student.__str__(last_name):
            if student.last_name == last_name:
                return student




    # def compar_student(self, last_name):
    #     for i in str(Student.__str__):
    #         if i.last_name == last_name:
    #             return i


#v1
    # def comparison_student(self, name):
    #     for stdnt in self.group:
    #         if name in stdnt:
    #             return Student.__str__(name)
#v2
    # def compar_student(self, last_name):
    #     for student in self.group:
    #         if student.last_name == last_name:
    #             return student


#v3
    # def compar_student(self, name):
    #     if name in Student.__str__(name):
    #         return Student.__str__(name)

#v4
# def compar_student(self, last_name):
#     for student in Group.group:
#         if student.last_name == last_name:
#             return Student.__str__(last_name)


            # if name in Student.__str__(name):
            #     return
            # gr = Group('PD1')

# self.group = set()      gr = Group('PD1')
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'



        # print(gr.__str__(self, name))
        # for student in self.__str__:
        #     if student.name == name:
        #         return student
        # return True for i in Student.__str__(self) if i == *args:
            # if student.args == last_name:
            #     return student
    #
    # def find_student(self, last_name):
    #     for student in self.group:
    #         if student.last_name == last_name:
    #             return student



