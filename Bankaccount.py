class Account():
    # Basic Init function to initialize all attributes
    def __init__(self, balance=0, owner):
        self.balance = balance
        self.owner = owner
    
    # Function that can withdraw money and checks if the withdrawal amount is higher than the balance
    def withdrawal(self, balance, wd_amount):
        if wd_amount > self.balance:
            print("Unefficent Funds")
        else:
            self.balance = self.balance - wd_amount

    # A function that can deposit money 
    def deposit(self, balance, d_amount):
        self.balance = self.balance + d_amount

    # Displays Account Information
    def return_string(self, balance, owner):
        print("Name of Owner: {y}".format(y=self.owner))
        print("Numbers of dollars: {x}".format(x=self.balance))

