
class Employee:
    def __init__(self, name, position, salary, raise_amount):
        self.name = name.lower
        self.position = position.lower
        self.salary = salary
        self.raise_amount = raise_amount
        

    def set_salary(self, set_amaount):
        self.salary = set_amaount
        
    def set_raise(self, set_rasie):
        self.raise_amount = set_rasie

    def give_raise(self):
        self.salary = self.salary * self. raise_amount
        
    def get_salary(self):
        return int(self.salary)
        
    def get_position(self):
        return self.position

    def get_raise(self):
        return self.raise_amount

class Student:
    def __init__(self, name, standard, group, roll, student_type):
        self.name = name
        self.standard = standard
        self.group = group
        self.roll = roll
        self.student_type = student_type
        
    def get_group(self):
        return self.group
            
    def get_type(self):
        return self.student_type
                

class Club:

        def __init__(self, name, max_member):
            self.name = name.lower
            self.members = []
            self.max_member = max_member
        
        def add_member(self, name):
            if len(self.members) >= self.max_member:
                return False
            else:
                self.members.append(name.name.lower())
                return True    

        def get_members(self):
            return self.members

        def Kick(self, name):
            self.members.remove(name.name.lower())





emp1 = Employee("Arif", "Teacher", 25000, 1.10)
emp2 = Employee("Rony", "jainator", 3000, 1.05)
emp3 = Employee("Hermione", "Vice Principal", 35000, 1.20)
student1 = Student("Jimmy", 9, "Science", 5, "Bright")
student2 = Student("Max", 9, "Science", 2, "Bright")
student3 = Student("Huel", 9, "commerece", 14, "Average")
student4 = Student("Scarlet", 10, "Arts", 23, "Dull")


#print(emp1.get_position())
#print(emp1.get_salary())
#print(emp1.get_raise())
#emp1.give_raise()
#print(emp1.get_salary())


science_club = Club('Science', 10)

science_club.add_member(student1)
science_club.add_member(student4)


#print(science_club.get_members())
science_club.Kick(student4)
#print(science_club.members)

print(Employee)