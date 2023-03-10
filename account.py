#! /usr/bin/python

from datetime import datetime

import transaction


class Account:
    """Represents account data

    Attributes
    ----------
    acc_number: int, account number
    acc_name: str, account name, must contain at least 4 characters
    transactions: list, all current account transactions
    balance: float, account balance, represents sum of all transactions amount
    all_usd: bool, shows, is all account transactions use USD currency

    Methods
    -------
    add_transaction: adds new transaction to account's transactions list
    """

    def __init__(self, acc_number: int, acc_name: str, transactions: list=None):
        self.__acc_number = acc_number
        self.acc_name = acc_name
        self.__transactions = list()
        if transactions:
            self.__transactions.extend(transactions)

    @property
    def acc_number(self):
        return self.__acc_number

    @property
    def acc_name(self):
        return self.__acc_name

    @acc_name.setter
    def acc_name(self, val: str):
        if len(val) < 4:
            raise ValueError('Account name must contain at least 4 characters')
        else:
            self.__acc_name = val

    @property
    def balance(self):
        bal = 0.0
        for tr in self.__transactions:
            bal += tr.usd
        return bal

    @property
    def all_usd(self):
        for tr in self.__transactions:
            if tr.currency != 'USD':
                return False

        return True

    def __len__(self):
        return len(self.__transactions)

    def __repr__(self):
        return object.__repr__(self)

    def __str__(self):
        return (
            f"Account {self.__acc_number}: {self.__acc_name}. Balance: {self.balance}"
        )

    def add_transaction(self, tr: transaction.Transaction):
        """
        Adds new transaction object to transactions list
        :param tr: Transaction object
        :return: None
        """
        self.__transactions.append(tr)


if __name__ == "__main__":
    acc = Account(100500, 'qwerty', [transaction.Transaction(100, datetime.now()), transaction.Transaction(-300, datetime.now(), currency='RUB', usd_conversion_rate=0.0135)])
    acc.add_transaction(transaction.Transaction(-50, datetime.now()))

    print(f'acc_name: {acc.acc_name}')
    print(f'acc_number: {acc.acc_number}')
    print(f'all_usd: {acc.all_usd}')
    print(f'balance: {acc.balance}')
    print(f'Transactions count: {len(acc)}')
