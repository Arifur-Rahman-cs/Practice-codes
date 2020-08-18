class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):

        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0

        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Arif", 18, 75)
s2 = Student("Rafi", 18, 85)
s3 = Student("salem", 21, 91)


course_1 = Course("Science", 5)

course_1.add_student(s1)
course_1.add_student(s2)
course_1.add_student(s3)

print(course_1.get_average_grade())
