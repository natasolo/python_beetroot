# Make a class structure in python representing people in a school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to the different classes,
# and keep in mind which are common and which are not.
# For example name should be a Person attribute,
# while salary should only be available to Teacher.


class Person:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def full_name(self):
        print(f"{self.first_name} {self.last_name}")


class Student(Person):

    def __init__(self, first_name, last_name, phone_number, transcript_id, group):
        super().__init__(first_name, last_name, phone_number)
        self.transcript_id = transcript_id
        self.group = group
        self.transcript = {}

    def add_to_transcript(self, subject, mark):
        self.transcript[subject] = mark

    def print_transcript(self):
        print(self.transcript)

    def get_average_mark(self):
        self.average_mark = sum(self.transcript.values()) / len(self.transcript.values())

        print(f'average_mark is {self.average_mark}')


student_1 = Student('Mike', 'Smith', '097806543', 'st14357', 'PA14-27')
student_2 = Student('Nikolas', 'Cage', '098866346', 'st15487', 'PA14-25')

student_1.add_to_transcript('maths', 93)
student_1.add_to_transcript('physics', 84)
student_1.full_name()
student_1.print_transcript()
student_1.get_average_mark()


class Teacher(Person):
    def __init__(self, first_name, last_name, phone_number, subject, students=None):
        super().__init__(first_name, last_name, phone_number)
        self.subject = subject
        self.students = students or []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def print_student(self):
        for student in self.students:
            student.full_name()
            print(student.group)


teacher_1 = Teacher('Scott', 'White', '93879876', 'Maths', [student_2])
teacher_2 = Teacher('Mary', 'Lee', '098765433', 'Physics', [student_1])

teacher_1.full_name()
teacher_2.add_student(student_2)
teacher_2.print_student()
