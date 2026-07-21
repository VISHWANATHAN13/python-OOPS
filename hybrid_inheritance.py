class A:
    def fun1(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.fun1()