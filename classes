class BankAccount():
    def __init__(self, accountNumber, bank_name, owner, balance=0):
      self.accountNumber = accountNumber
      self.balance = balance
      self.owner = owner
      self.bank_name = bank_name
      self.owner.bank_accounts.append(self)
        
    def get_balance(self):
      return self.balance
        
    def deposit(self, amount):
      if amount >= 1000000000:
        print(f"No te crees nitú que la cantidad de {amount} existe")
        return False
      elif amount <= 0:
        print(f"¿Cómo vas a ingresar {amount} tronco?")
        return False
      else:
        self.balance += amount
        return True
        
    def withdraw(self, amount):
      new_balance = self.balance - amount
      if new_balance >= 0:
        self.balance = new_balance
        return True
      else:
        print("No tienes un duro, no puedes sacar, eres pobre")
        return False
        
    def deposit_with_print(self,amount):
      deposit_success = self.deposit(amount)
      if deposit_success:
        print(f"has ingresado {amount}, ahora tienes {self.balance}")
      else:
        print(f"algo ha fallado")
      
    def withdraw_with_print(self,amount):
      withdraw_success = self.withdraw(amount)
      if withdraw_success:
        print(f"has sacado {amount}, ahora tienes {self.balance}")
      else:
        print(f"el máximo que puedes sacar es {self.balance}")
        
    def __str__(self):
      cadena = f"La cuenta {self.accountNumber}, es de {self.owner.name} y tiene {self.balance} dineros."
      return cadena
      
      
      
class Owner:
  def __init__(self, name):
    self.name = name
    self.bank_accounts = []
    
  def get_bank_accounts(self):
    accounts_with_money = []
    for bank_account in self.bank_accounts:
      if bank_account.get_balance() > 0:
        bank_account_ref = f"{bank_account.bank_name}: {bank_account.accountNumber}"
        accounts_with_money.append(bank_account_ref)
    return accounts_with_money
    
  def print_bank_accounts(self):
    pass
    
