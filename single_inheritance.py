class Father:
    def house(self):
        print("House")

class Son(Father):
    def bike(self):
        print("Bike")

s = Son()

s.house()
s.bike()