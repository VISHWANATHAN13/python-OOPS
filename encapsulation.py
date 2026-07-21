class Bank:

    def __init__(self):
        self.__balance = 5000
    def showBalance(self):
        print(self.__balance)
    
b = Bank()
b.showBalance()
# print(b.__balance)  error