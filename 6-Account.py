
class Account(object):

    def __init__(self,  initial_amount):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        s = '%s, %s, balance: %s' % \
            ( self.balance)
        print (s)


a1 = Account(0)
a1.deposit(100)
a1.deposit(200)
a1.withdraw(50)
a1.deposit(100)
a1.withdraw(250)
a1.deposit(30)
print ("a1's balance:", a1.balance)