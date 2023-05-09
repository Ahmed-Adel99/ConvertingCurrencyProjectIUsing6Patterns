# In the Dependency Injection pattern,
# the exchange rate strategy is passed to the MoneyChanger class as a constructor argument,
# which makes the MoneyChanger class more flexible and allows us to easily
# swap different exchange rate strategies at runtime.

'''
The code uses Dependency Injection to create objects of SimpleExchangeRate, ComplexExchangeRate,
MoneyChanger, and MoneyConverter classes. This allows us to inject a dependency (an object of one class)
into another class, without creating objects inside a class.
'''


class ExchangeRate:
    def get_rate(self, from_currency, to_currency):
        pass


class SimpleExchangeRate(ExchangeRate):
    def __init__(self, rates):
        self._rates = rates

    def get_rate(self, from_currency, to_currency):
        return self._rates[from_currency][to_currency]


class ComplexExchangeRate(ExchangeRate):
    def __init__(self, base_currency, rates):
        self._base_currency = base_currency
        self._rates = rates

    def get_rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1.0
        elif from_currency == self._base_currency:
            return self._rates[to_currency]
        elif to_currency == self._base_currency:
            return 1 / self._rates[from_currency]
        else:
            return self._rates[to_currency] / self._rates[from_currency]


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


class MoneyChanger:
    def __init__(self, exchange_rate_strategy):
        self._exchange_rate_strategy = exchange_rate_strategy

    def change_money(self, money, to_currency):
        from_currency = money.currency
        rate = self._exchange_rate_strategy.get_rate(from_currency, to_currency)
        new_amount = money.amount * rate
        new_money = Money(new_amount, to_currency)
        return new_money


class MoneyConverter:
    def __init__(self, money_changer):
        self._money_changer = money_changer

    def change_money(self, money, to_currency):
        return self._money_changer.change_money(money, to_currency)


# Creating objects using dependency injection
simple_exchange_rate = SimpleExchangeRate(
    {'USD': {'EUR': 0.85, 'GBP': 0.75}, 'EUR': {'USD': 1.18, 'GBP': 0.88}, 'GBP': {'USD': 1.34, 'EUR': 1.14}})

complex_exchange_rate = ComplexExchangeRate('USD', {'EUR': 0.85, 'GBP': 1.25})

money_changer = MoneyChanger(complex_exchange_rate)
money_converter = MoneyConverter(money_changer)

# Using the MoneyConverter to convert money
money = Money(15, 'EUR')
new_money = money_converter.change_money(money, 'USD')
print(f'{money.amount} {money.currency} is equivalent to {new_money.amount} {new_money.currency}')
