from abc import ABC, abstractmethod
#In the Strategy pattern,

# we create separate classes for each exchange rate strategy that implement a common interface.

# We pass an instance of one of these classes to the MoneyChanger class

# which uses it to get the exchange rate.

# This approach allows us to easily add new exchange rate strategies
# by implementing the ExchangeRateStrategy interface.
'''
The ExchangeRate class is an abstract class, and SimpleExchangeRate and ComplexExchangeRate classes
are concrete classes that implement the get_rate() method in their way. 
MoneyChanger uses the ExchangeRate class to calculate the exchange rate, 

which means the "MoneyChanger" class is independent of the implementation details of the "exchange rate".
'''
class ExchangeRateStrategy(ABC):
    @abstractmethod
    def get_rate(self, from_currency, to_currency):
        pass
class SimpleExchangeRate(ExchangeRateStrategy):
    def __init__(self, rates):
        self._rates = rates

    def get_rate(self, from_currency, to_currency):
        return self._rates[from_currency][to_currency]

class ComplexExchangeRate(ExchangeRateStrategy):
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


# Creating objects using the Strategy pattern
simple_exchange_rate = SimpleExchangeRate({
    'USD': {'EUR': 0.85, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'GBP': 0.88},
    'GBP': {'USD': 1.34, 'EUR': 1.14}
})

complex_exchange_rate = ComplexExchangeRate('USD', {
    'EUR': 0.85,
    'GBP': 1.25
})

# Using the Strategy pattern to set the exchange rate strategy
money_changer = MoneyChanger(simple_exchange_rate)
money_converter = MoneyConverter(money_changer)

# Using the MoneyConverter to convert money
money = Money(100, 'GBP')
new_money = money_converter.change_money(money, 'USD')
print(f'{money.amount} {money.currency} is equivalent to {new_money.amount} {new_money.currency}')

# Using the Strategy pattern to change the exchange rate strategy
money_changer._exchange_rate_strategy = complex_exchange_rate
new_money = money_converter.change_money(money, 'EUR')
print(f'{money.amount} {money.currency} is equivalent to {new_money.amount} {new_money.currency}')