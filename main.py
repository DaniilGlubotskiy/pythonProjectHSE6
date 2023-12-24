class Account:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(('deposit', amount))
            print(f"Депозит на сумму {amount} успешно проведен. Новый баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(('withdraw', amount))
            print(f"Снятие на сумму {amount} успешно проведено. Новый баланс: {self.balance}")
        elif amount > self.balance:
            print("Недостаточно средств для снятия.")
        else:
            print("Сумма для снятия должна быть положительной и не превышать текущий баланс.")

    def show_transaction_history(self):
        print("История операций:")
        for operation_type, amount in self.transaction_history:
            print(f"{operation_type.capitalize()}: {amount}")


name = input("Введите имя для создания банковского аккаунта: ")
initial_balance = float(input("Введите начальный баланс: "))

# Создаем аккаунт
account = Account(name, initial_balance)

# Вносим депозит
deposit_amount = float(input("Введите сумму для депозита: "))
account.deposit(deposit_amount)

# Снимаем деньги
withdraw_amount = float(input("Введите сумму для снятия: "))
account.withdraw(withdraw_amount)

# Показываем историю операций
account.show_transaction_history()
