class Employee:
    def __init__(self, name, salary, raise_amount):
        self.name = name
        self.salary = salary
        self.raise_amount = raise_amount
    
    def set_raise(self, new_raise):
        self.raise_amount = new_raise

    def give_raise(self):
        self.salary = self.salary * self.raise_amount

    def get_salary(self):
        return self.salary


class Teacher(Employee):
    def __init__(self, name, salary, raise_amount, subject):
        super().__init__(name, salary, raise_amount)
        self.subject = subject

teacher = Teacher("Amjad", 25000, 1.10, "Chemistry")
emp1 = Employee("Imtiaz", 5000, 1.05)

print(teacher.get_salary())
teacher.give_raise()
print(teacher.get_salary())

print(emp1.get_salary())
teacher.give_raise()
print(emp1.get_salary())

teacher.set_raise(1.20)
emp1.set_raise(1.10)

print(teacher.get_salary())
print(emp1.get_salary())