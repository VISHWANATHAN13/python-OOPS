class GrandFather:
    def land(self):
        print("Land")

class Father(GrandFather):
    def house(self):
        print("House")

class Son(Father):
    def bike(self):
        print("Bike")

s = Son()

s.land()
s.house()
s.bike()