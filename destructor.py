class Student:

    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")

s = Student()

del s #call statement to destroy objects