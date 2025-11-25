"""
Финальная задача №1
https://stepik.org/lesson/2022462/step/1?unit=2050885

Легенда:
Вы разрабатываете ядро для простого банковского приложения.
Вам нужно создать систему классов, которая будет представлять банковский счет и связанные с ним транзакции.

Техническое задание:
Ваша задача — реализовать три класса: Transaction, AccountError и Account.
Шаблон кода ниже содержит полную систему тестов, которая проверит каждый аспект вашей реализации.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Transaction:
    amount: float
    description: str

class AccountError(Exception):
    pass

class TransactionError(AccountError):
    pass

class Account:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._initial_balance = initial_balance
        self._transactions = []

    @property
    def balance(self):
        return self._initial_balance + sum(transaction.amount for transaction in self._transactions)

    def add_transaction(self, transaction: Transaction):
        if self.balance + transaction.amount < 0:
            raise TransactionError("Транзакция невозможна: недостаточно средств.")
        else:
            self._transactions.append(transaction)

    @classmethod
    def from_csv(cls, csv_string: str):
        own, balance = csv_string.split(",")
        return cls(own, float(balance))

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f"Счет {self.owner}"

    def __repr__(self):
        return f"Account(owner='{self.owner}', initial_balance={self.balance})"