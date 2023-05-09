'''
The Singleton class ensures that only one instance of the MoneyChanger class is created throughout
the program's lifetime. This is achieved by using a private class variable _instance,
which holds the reference to the single instance of the class
'''

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

class MoneyChanger(Singleton):
    def __init__(self):
        self._exchange_rates = {
            "USD": {"EUR": 0.82, "GBP": 0.72},
            "EUR": {"USD": 1.22, "GBP": 0.87},
            "GBP": {"USD": 1.39, "EUR": 1.14}
        }

    def get_exchange_rate(self, from_currency, to_currency):
        return self._exchange_rates[from_currency][to_currency]

    def change_money(self, money, to_currency):
        from_currency = money.currency
        rate = self.get_exchange_rate(from_currency, to_currency)
        new_amount = money.amount * rate
        new_money = Money(new_amount, to_currency)
        return new_money


money_changer1 = MoneyChanger()

money1 = Money(100, "USD")
new_money1 = money_changer1.change_money(money1, "EUR")



print(money1.amount,money1.currency,"is equivalent to",new_money1.amount, new_money1.currency)  # 82.0 EUR


