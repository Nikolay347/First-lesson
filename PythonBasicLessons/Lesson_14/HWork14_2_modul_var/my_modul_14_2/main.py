# my_modul_14_2/main.py
# from PythonBasicLessons.Lesson_14.HWork14_1_modul_var.my_modul_14_1 import Human

from student import Student
from group import Group
from group_lim_reach_exception import GroupLimitReachedException
gr = Group('PD1')

## v.1 Checking
def main():
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


    assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    assert gr.find_student('Lempi') == st10
    assert gr.find_student('Jobs2') is None
    gr.delete_student('Taylor')
    print(gr)
    print("Verification v1 good!")
    print()

if __name__ == '__main__':      #Verification main.py as main file
    main()
#############################################################################################################

#v.2 Checking
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 27, 'Malik', 'Kurd', 'AN142')
#...further formation of students depending on the number of inspections and the number of the student

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(gr)
assert gr.find_student('Kurd') == st3  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr.add_student(st1)
gr.add_student(st2)
print("Verification v2 good!")




# def form_stud():
#     # st = "st" + (input("Input number of student (1, 2, ...): "))
#     return str(''.join(f"{input("Input gender: " ) }, {input("Input age: " ) }, {input("Input first_name: " ) }, {input("Input last_name: ")}, {input("Input record_book(AN142/AN145): ")}"))
# # st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# # print(form_stud())


