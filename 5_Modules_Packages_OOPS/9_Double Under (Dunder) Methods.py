class Employee:
    def __init__(self, name, age):
        self.emp_name = name
        self.emp_age = age

    def __str__(self):
        return self.emp_name + "'s age is " + str(self.emp_age)

    def __len__(self):
        return len(self.emp_name)

tom = Employee("Venkat Vala", 29)

print(tom)
print(len(tom))