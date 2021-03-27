

class Name():
    def __init__(self):
        self.cust_name = ""
        self.cust_name2 = ""
    def get_cust_info(self):
        self.cust_name = input("Enter Your Name:")

    def uppercase(self):

        return self.cust_name.upper()



customer1 = Name()
customer1.get_cust_info()
print (customer1.uppercase())
