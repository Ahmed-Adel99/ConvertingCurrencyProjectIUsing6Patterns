'''
Observable is a base class for observable objects, which are objects that maintain a list of

their observers and notify them of any changes to their state.

It has methods to add and remove observers from its list,
as well as to notify all observers of changes.
'''
class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

class MoneyChanger(Observable):
    def __init__(self):
        super().__init__()
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
        self.notify_observers(money, new_money)
        return new_money

class Logger:
    def update(self, observable, *args, **kwargs):
        money, new_money = args
        print(f"{money.amount} {money.currency} was changed to {new_money.amount} {new_money.currency}")






money_changer = MoneyChanger()
logger = Logger()
money_changer.add_observer(logger)

money = Money(200, "EUR")
new_money = money_changer.change_money(money, "USD")










