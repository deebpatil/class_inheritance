class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

    def show_details(self):
        print("Personal Details")
        print("Name: ",self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated .$",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount>self.balance:
            print("Insufficient balance :",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance now is : $",self.balance)

    def view_balance(self):
        self.show_details()
        print("Amount balance is :$",self.balance)

M = User("Deepali",27,"female")
M.show_details()
C = Bank("mukesh",30,"male")
(C.deposit(2000))
(C.withdraw(3000))
(C.deposit(1000))
(C.withdraw(2000))
(C.view_balance())