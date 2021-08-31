class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.02, 0)

    def make_deposit(self, amount):	
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self


class BankAccount:

    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance+= amount
        return self
    def withdraw(self, amount):
        if(amount < self.balance): 
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= (1+self.int_rate)
        return self

andrew = User("Andrew Shaw", "andrew@python.com")
andrew.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(50).display_user_balance()
james = User("James Wongsudin", "james@python.com")
james.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()
mason = User("Mason Holland", "mason@python.com")
mason.make_deposit(250).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()