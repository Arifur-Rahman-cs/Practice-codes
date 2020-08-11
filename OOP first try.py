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
        self.student = []

    def add_student(self, student):

        if len(self.student) < max_student:
            self.student.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0

        for student in self.student:
            value += self.get_grade

        return value / len(self.student)


s1 = Student("Arif", 18, 75)
s2 = Student("Rafi", 18, 85)
s3 = Student("salem", 21, 91)

print(Course.get_average_grade())


