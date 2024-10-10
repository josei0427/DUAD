class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        print(f"Se ha depositado {amount}. Nuevo balance: {self.balance}")

    def substract_money(self, amount):
        self.balance -= amount
        print(f"Se ha retirado {amount}. Nuevo balance: {self.balance}")


class SavingsAccount(BankAccount):
    min_balance = 20
    def substract_money(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"No se puede retirar {amount}. El balance mínimo debe ser {self.min_balance} y el balance actual es: {self.balance}")
        else:
            BankAccount.substract_money(self, amount)


new_account = SavingsAccount(balance= 0)
new_account.add_money(100)
new_account.substract_money(60)
new_account.substract_money(45)
