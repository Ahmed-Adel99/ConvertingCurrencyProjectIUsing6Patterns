class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

class MoneyChanger:
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
'''
The MoneyModel class represents the model in the MVC pattern. 
It stores the current amount and currency of the money being displayed and provides methods 
to update them and to convert to a new currency.
'''
class MoneyModel:
    def __init__(self):
        self._money = Money(0, "USD")
        self._money_changer = MoneyChanger()

    def get_money(self):
        return self._money

    def set_money(self, amount, currency):
        self._money.amount = amount
        self._money.currency = currency

    def change_money(self, to_currency):
        self._money = self._money_changer.change_money(self._money, to_currency)

'''
The MoneyView class represents the view in the MVC pattern. 
It displays the current money amount and currency.
'''
class MoneyView:
    def __init__(self, model):
        self._model = model

    def display(self):
        money = self._model.get_money()
        print(f"{money.amount:.2f} {money.currency}")
'''
The MoneyController class represents the controller in the MVC pattern. 
It receives user input and updates the model accordingly.
'''
class MoneyController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def set_money(self, amount, currency):
        self._model.set_money(amount, currency)

    def change_money(self, to_currency):
        self._model.change_money(to_currency)
        self._view.display()

model = MoneyModel()
view = MoneyView(model)
controller = MoneyController(model, view)

controller.set_money(100, "USD")

controller.change_money("EUR")  # Outputs: 82.00 EUR
