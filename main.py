class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Сумма {amount} руб. успешно внесена на счет {self.account_number}. Новый баланс: {self.balance} руб.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Сумма {amount} руб. успешно снята со счета {self.account_number}. Новый баланс: {self.balance} руб.")
        else:
            print("Ошибка: Недостаточно средств на счете.")

    def get_balance(self):
        return self.balance


# Создание двух экземпляров класса BankAccount
account1 = BankAccount("123456789", "Иванов")
account2 = BankAccount("987654321", "Петров", 1000)

# Внесение и снятие денег на счетах
account1.deposit(500)
account1.withdraw(200)
account2.withdraw(1500)

# Получение баланса счетов
balance1 = account1.get_balance()
balance2 = account2.get_balance()

# Вывод баланса счетов
print(f"Баланс счета {account1.account_number}: {balance1} руб.")
print(f"Баланс счета {account2.account_number}: {balance2} руб.")
