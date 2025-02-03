#my_modul_14_1/group.py

from group_lim_reach_exception import GroupLimitReachedException

class Group:

    def __init__(self, number, student_limit = 10):
        # Initiation by attributes of the class group object. Instance attributes. No inheritance.
        self.number = number
        self.group = set()
        self.student_limit = student_limit


    def add_student(self, student):
        from datetime import datetime                       #import function datetime from datetime module
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(f"{str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}\n Attempting to exceed the number {self.student_limit} of group! Fixation it at list in the log_Exception.txt. ", f"Received group: {str(gr)} {Group.__str__(self)}")
        self.group.add(student)


    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__() + "\n "
        return f'Number:{self.number} \n {all_students} '



gr = Group('PD1')


