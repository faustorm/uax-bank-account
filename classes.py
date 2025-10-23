class BankAccount():
    def __init__(self, accountNumber, bank_name, owner, balance=0, currency = "EUR"):
      self.accountNumber = accountNumber
      self.balance = balance
      self.owner = owner
      self.bank_name = bank_name
      self.owner.bank_accounts.append(self)
      self.currency = currency
        
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
    
    #calcular TAE
    def calcular_tae_diario(self, tin, dias):
      frecuencia_pagos = 12 #pago mensual
      tae = (1 + tin / frecuencia_pagos) ** frecuencia_pagos - 1
      return tae
    
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
        bank_account_ref = f"{bank_account.bank_name}: {bank_account.accountNumber} -> {bank_account.balance} {bank_account.currency}"
        accounts_with_money.append(bank_account_ref)
    return accounts_with_money
    
  def print_bank_accounts(self):
    pass

class SavingsAccount(BankAccount):
  def __init__(self, accountNumber, bank_name, owner, interest_rate = 4, balance=0):
    super().__init__(accountNumber, bank_name, owner, balance)
    self.interest_rate = interest_rate

  def interestGenerated(self, number_of_days = 0):
    tae = self.calcular_tae_diario(self.interest_rate, number_of_days)
    interes_generado = self.balance * tae/100
    return interes_generado
  
  
class CheckingAccount(BankAccount):
  def __init__(self, accountNumber, bank_name, owner, balance=0, currency="EUR"):
    super().__init__(accountNumber, bank_name, owner, balance, currency)
    self.interest_rate = 0.08
    self.credit_limit = 2000
    self.current_credit = 0
    self.available_credit = self.credit_limit - self.current_credit

  def getCreditLimit(self):
    return self.credit_limit
  
  def withdraw(self, amount):
    if self.available_credit > amount and amount < self.credit_limit and amount > 0:
      self.current_credit += amount
      self.available_credit -= amount
      return True
    else:
      print("Zorry Vro")
      return False
  
  def get_credit_to_pay(self):
    number_of_days = 30
    tae = self.calcular_tae_diario(self.interest_rate, number_of_days)
    interes_generado = self.current_credit * tae/100
    total_credit = self.current_credit +  interes_generado
    return total_credit
