#! /usr/bin/python

from datetime import datetime


class Transaction:
    """Represents single transaction data

    Attributes
    ----------
    amount: float, transaction amount
    date: datetime, transaction date
    currency: transaction currency, USD by default
    usd_conversion_rate: float, transaction currency rate against the USD
    description: str, transaction description
    usd: float, transaction amount in usd

    """

    def __init__(self, amount: float, date: datetime, currency: str='USD', usd_conversion_rate: float=1.0, description: str=None):
        if usd_conversion_rate > 0:
            self.__usd_conversion_rate = usd_conversion_rate
        else:
            raise ValueError('Conversion rate must be greater than 0!')

        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate

    @property
    def description(self):
        return self.__description

    def __repr__(self):
        return object.__repr__(self)

    def __str__(self):
        return (
            f"{self.__date} transaction {self.__amount} {self.__currency}{', ' + str(self.usd) + 'USD' if self.__usd_conversion_rate != 1 else ''}"
            f"{', ' + self.__description if self.__description else ''}"
        )


if __name__ == "__main__":
    tr = Transaction(amount=1.0, date=datetime.now())

    print(f'amount: {tr.amount}')
    print(f'currency: {tr.currency}')
    print(f'date: {tr.date}')
    print(f'usd_conversion_rate: {tr.usd_conversion_rate}')
    print(f'usd: {tr.usd}')
    print(f'description: {tr.description}')
