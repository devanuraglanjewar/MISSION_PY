# Wrapping data and function into a single unit (object)
# Example
class BankAccount:
  def __init__(self, balance):
    self._balance = balance  # Private attribute

  def get_balance(self):
    return self._balance  # Public method to access balance

  def deposit(self, amount):
    self._balance += amount  # Private attribute modified within the class

# Create an instance
account1 = BankAccount(100)

# Direct access to private attribute is discouraged (convention)
# print(account1._balance)  # Avoid this

# Access balance through the public method
print(account1.get_balance())  # Output: 100

# Deposit using the public method
account1.deposit(50)
print(account1.get_balance())  # Output: 150