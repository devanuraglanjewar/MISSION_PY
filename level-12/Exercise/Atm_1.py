# create account class with 2 attributes - balance and account no,
# careate method for debit,credit & balance
class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance =balance
    
    def debit(self,ammount):
        if (self.balance >= ammount):
            now = self.balance - ammount
            print(ammount,"Rs. is debited from your account")
            print("Your new Balance is ",now)
        else:
            print("invalid amount")
    def credit(self,ammount):
            now = self.balance + ammount
            print(ammount,"Rs. is credit in your account")
            print("Your new Balance is ",now)


a1=Account(10001,1000)
a1.debit(500)
a1.credit(700)
