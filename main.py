from classes import BankAccount, Owner

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
