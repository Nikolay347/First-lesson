# Students group
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

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        # Initiation by attributes of the class Student object. Instance attributes. Inheritance from human.
        super().__init__(gender, age, first_name, last_name)    # is an override from human
        self.record_book = record_book                          # new definition

    def __str__(self):
        # Defining a custom string representation of an object.
        return super().__str__() + f", {self.record_book}"  # is an override from human + new definition

    # def number(self):

class Group:

    def __init__(self, number):
        # Initiation by attributes of the class group object. Instance attributes. No inheritance.
        self.number = number
        self.group = set()

    def add_student(self, student):
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
            all_students += student.__str__() + "\n"
        return f'Number:{self.number} \n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

# check and validation:
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
print("All done!")