"""Simple Bank System
https://leetcode.com/problems/simple-bank-system
"""


class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            0 < account1 <= self.n and 0 < account2 <= self.n
            and money <= self.balance[account1 - 1]
        ):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 < account <= self.n:
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 < account <= self.n and money <= self.balance[account - 1]:
            self.balance[account - 1] -= money
            return True
        return False


bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))
