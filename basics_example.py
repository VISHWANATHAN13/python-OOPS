class Employee:
    # static variable
    college = "panimalar"
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary

e1 = Employee("vishwa",20_000)
print(e1.name)
print(e1.salary)
print(e1.college)