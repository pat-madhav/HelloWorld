class Student:
    school = 'SJPS'

    # Instance method - Has something to do with INSTANCE VARIABLES
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # Class method - Has something to do with CLASS VARIABLES
    @classmethod
    def get_school(cls):
        return Student.school

    # Static method
    @staticmethod
    def student_benefits():
        print('Student discount = {0}%'.format('FuckOff'))

# ------------------------------------------
# Creating instance/objects using the class - Student
s1 = Student(73, 50, 95)

# Calling INSTANCE METHOD
print(s1.avg())

# Calling CLASS METHOD
print(Student.get_school())

# Calling STATIC method
Student.student_benefits()

