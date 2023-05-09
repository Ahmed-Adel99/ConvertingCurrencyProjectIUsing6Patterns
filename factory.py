
'''
The main class hierarchy includes a Money base class and its three subclasses,
SDMoney, EURMoney, and GBPMoney. The MoneyFactory class contains a static method,
create_money, that accepts the currency type and amount as arguments and returns an instance
of the corresponding money subclass.

The CurrencyConverter class uses the MoneyFactory class to create instances of the appropriate Money
subclass. It then uses exchange rates to convert the amount from one currency to another.
'''
class Money:
    def __init__(self, amount):
        self.amount = amount

class USDMoney(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.currency = "USD"

class EURMoney(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.currency = "EUR"

class GBPMoney(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.currency = "GBP"

class MoneyFactory:
    @staticmethod
    def create_money(currency, amount):
        if currency == "USD":
            return USDMoney(amount)
        elif currency == "EUR":
            return EURMoney(amount)
        elif currency == "GBP":
            return GBPMoney(amount)
        else:
            raise Exception("Invalid currency")

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            "USD": {"USD": 1, "EUR": 0.82, "GBP": 0.72},
            "EUR": {"USD": 1.22, "EUR": 1, "GBP": 0.87},
            "GBP": {"USD": 1.39, "EUR": 1.14, "GBP": 1}
        }

    def convert(self, amount, from_currency, to_currency):
        from_money = MoneyFactory.create_money(from_currency, amount)
        to_money = MoneyFactory.create_money(to_currency, 0)

        rate = self.exchange_rates[from_money.currency][to_money.currency]
        converted_amount = rate * from_money.amount

        to_money.amount = converted_amount
        return to_money.amount


# Create an instance of CurrencyConverter
converter = CurrencyConverter()

# Convert $100 to EUR
amount = 100
from_currency = "USD"
to_currency = "EUR"


converted_amount = converter.convert(amount, from_currency, to_currency)

# Output the converted amount
print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")
