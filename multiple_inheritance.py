class Father:
    def house(self):
        print("House")

class Mother:
    def jewels(self):
        print("Jewels")

class Son(Father, Mother):
    pass

s = Son()

s.house()
s.jewels()