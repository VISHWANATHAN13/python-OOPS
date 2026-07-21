class Parent:
    def property(self):
        print("Property")

class Son(Parent):
    pass

class Daughter(Parent):
    pass

Son().property()
Daughter().property()