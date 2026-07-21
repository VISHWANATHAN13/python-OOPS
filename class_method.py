class Employee:
    college="panimalar"

    @classmethod
    def show_college(cls):
        print(cls.college)

Employee.show_college()