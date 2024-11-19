from collections import namedtuple
Student = namedtuple('student',['name','age','rollno'])
students = []

def add_record():
    name = input('Enter student name: ')
    age = input('Enter student age: ')
    rollno = input('Enter student roll number: ')
    student = Student(name=name,age=age,rollno=rollno)
    student.append(students)
    print("Record successfully added!")

def remove_record():
    rollno =input('Enter student roll number')
    for student in students:
        if student.rollno == rollno:
            students.remove(student)
            print("Record successfully deleted")
            break

        else:
            print("Record not found")


def veiw_record():
    for student in students:
        print(student)
