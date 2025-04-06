# Students group
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"{self.gender}. {self.age}, {self.first_name}, {self.last_name}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f", {self.record_book}"


class Group:
    def __init__(self, number, student_limit = 10):
        self.number = number,
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        from datetime import datetime
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(
                f"{str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}\n Attempting to exceed the number {self.student_limit} of group! Fixation it at list in the log_Exception.txt. ", f"Received group: {str(gr)} {Group.__str__(self)}")
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

class GroupLimitReachedException(Exception):    #Added for this HWork new class of exception from BaseException
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name
        self.log_error_data()

    def log_error_data(self):
        with open("../log_exceptions3.txt", "a") as file:
            file.write(f"\n".join(self.args)+ "\n")

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 27, 'Malik', 'Kurd', 'AN142')
st4 = Student('Female', 24, 'Monika', 'Lind', 'AN145')
st5 = Student('Male', 28, 'Arny', 'Rone', 'AN142')
st6 = Student('Female', 25, 'Elis', 'Shinny', 'AN145')
st7 = Student('Male', 31, 'Poll', 'Luise', 'AN142')
st8 = Student('Female', 25, 'Sindy', 'Woo', 'AN145')
st9 = Student('Male', 30, 'Daniel', 'Mur', 'AN142')
st10 = Student('Female', 26, 'Helen', 'Lempi', 'AN145')
st11 = Student('Female', 26, 'Unknown', 'Unknown', 'AN145')

gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)

except GroupLimitReachedException as error:
    print(error)
    print(gr)
except Exception as error:
    print(error)

assert gr.find_student('Jobs') == st1
print("All done!")