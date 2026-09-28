print("== Welcome to Student Management System ==")


class Student:

    def __init__(self, name, student_id, email, age, department, marks):

        self.name = name

        self.student_id = student_id

        self.email = email

        self.age = age

        self.department = department

        self.__marks = marks


    def display_info(self):

        print(f"Student Name : {self.name}")

        print(f"Student ID : {self.student_id}")

        print(f"Email : {self.email}")

        print(f"Age : {self.age}")

        print(f"Department : {self.department}")


    def calculate_result(self, bonus_mark=0):

        final_mark = self.__marks + bonus_mark

        if final_mark > 100:
            return "Invalid Mark"
        

        elif 80 <= final_mark <= 100:
            return "A+"


        elif 70 <= final_mark < 80:
            return "A"


        elif 60 <= final_mark < 70:
            return "B"


        elif 50 <= final_mark < 60:
            return "C"
 
 
        elif final_mark < 0:
                    return "Invalid Mark"
        else:
            return "F"


    def get_student_type(self):

        return "Student"



class UndergraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, marks, semester):

        Student.__init__(self, name, student_id, email, age, department, marks)

        self.semester = semester


    def display_info(self):

        Student.display_info(self)

        print(f"Semester : {self.semester}")


    def get_student_type(self):

        return "Undergraduate Student"



class GraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, marks, research_topic):

        Student.__init__(self, name, student_id, email, age, department, marks)

        self.research_topic = research_topic


    def display_info(self):

        Student.display_info(self)

        print(f"Research Topic : {self.research_topic}")


    def get_student_type(self):

        return "Graduate Student"



students = []


while True:

    print("Please enter 1 for Student")

    print("Please enter 2 for Undergraduate Student")

    print("Please enter 3 for Graduate Student")


    student_type = input("Please enter the student type : ")


    name = input("Please enter the student name : ")

    student_id = int(input("Please enter the student ID : "))

    email = input("Please enter the student email : ")

    age = int(input("Please enter the student age : "))

    department = input("Please enter the student department : ")

    marks = int(input("Please enter the student marks : "))


    if student_type == "1":

        student = Student(name, student_id, email, age, department, marks)


    elif student_type == "2":

        semester = int(input("Please enter the semester : "))

        student = UndergraduateStudent(name, student_id, email, age, department, marks, semester)


    elif student_type == "3":

        research_topic = input("Please enter the research topic : ")

        student = GraduateStudent(name, student_id, email, age, department, marks, research_topic)


    else:

        print("Invalid Student Type")

        choice = input("Please enter c to continue or press any button to exit : ")

        if choice == "c":
            continue

        else:
            break


    students.append(student)


    print("== Student Information ==")

    student.display_info()

    print(f"Student Type : {student.get_student_type()}")

    print(f"Student Result : {student.calculate_result()}")


    choice = input("Please enter c to continue or press any button to exit : ")

    if choice == "c":
        continue

    else:
        break



print("== All Student Information ==")


for student in students:

    student.display_info()

    print(f"Student Type : {student.get_student_type()}")

    print(f"Student Result : {student.calculate_result()}")



print("== Method Overloading Using Default Argument ==")


if len(students) > 0:

    print(f"Result without Bonus Mark : {students[0].calculate_result()}")

    print(f"Result with Bonus Mark : {students[0].calculate_result(5)}")



print("== Thank you so much for using my program ==")