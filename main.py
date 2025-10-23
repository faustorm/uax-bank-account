from classes import BankAccount, Owner, SavingsAccount, CheckingAccount

owner = Owner("Pepe")

cuenta1 = BankAccount("12345", "Sabadell", owner, 9)
cuenta2 = BankAccount("ABCDE", "BBVA", owner,950)
cuenta3 = BankAccount("XZSAA", "ING", owner)


print(cuenta1.get_balance())

cuenta1.deposit_with_print(-90)
print(cuenta1.get_balance())

cuenta1.withdraw_with_print(300)
print(cuenta1.get_balance())

print(cuenta1)
print("cuentas: ")
print(owner.get_bank_accounts())

cuentaAhorros1 = SavingsAccount("HF56565","Santander", owner)
cuentaAhorros1.deposit(85)
print(f"{cuentaAhorros1.interestGenerated(100):.2f} {cuentaAhorros1.currency}")

print(owner.get_bank_accounts())

cuentaCredito = CheckingAccount("XXX999", "Satander", owner)
cuentaCredito.withdraw(992)
print(f"A pagar el mes que viene (de momento): {cuentaCredito.get_credit_to_pay():.2f} {cuentaCredito.currency}")