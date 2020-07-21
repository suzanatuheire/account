class BankAccount:
    
   
    def __init__(self, first_name, last_name,bank,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number=phone_number
        self.bank=bank
   
    def account_name(self):
        name = "{} account for {} {}".format(
        self.bank, self.first_name, self.last_name)
        return name
   
    def account_name(self):
        name = "{} account for {} {}".format(
        self.bank, self.first_name, self.last_name)
        return name
   
    def deposit(self, amount):
        self.balance += amount
        print("You have deposited {} to your account".format(amount))
       
    def get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)
 

   

def withdraw(self, amount):
    if amount > 0:
        self.balance -= amount
        print("You have withdrawed {} to your account".format(amount))
def get_balance(self):
    return "The balance of {} is {} ".format(self.account_name(),self.balance)
    

def give_loan(self, loan):
    if loan <= 0:
        print()
        self.balance += loan
    else:
        print(""you have borrowed {}".format(loan)")

        def repay_loan(self, loan):
      if loan <= 0:
        print("Invalid amount to reduce your loan")
      else:
        self.loan_balance -= loan
        print(" You have repaid {}".format(loan))
























    
  
    
    
  

