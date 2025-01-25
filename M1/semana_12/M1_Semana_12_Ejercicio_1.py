"""1. Cree una clase de `BankAccount` que:
    a. Tenga un atributo de `balance`.
    b. Tenga un método para ingresar dinero.
    c. Tenga un método para retirar dinero.
    
    Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
    a. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
    b. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`."""


class InvalidRetrieveOfBalance(Exception):
    "Will raise an error if user tries to retrieve a quantity of money that would leave the account with an amount less than the min balance"
    pass


class NegativeMoneyQuantities(Exception):
    "Will raise an error if user tries to provide a negative quantity of money to any method"
    pass


def decorator_validate_positive_quantities(func):
    def wrapper(self, money_qty):
        try:
            if (money_qty < 0):
                raise NegativeMoneyQuantities
        except:
            print(f'-E-(decorator_validate_positive_quantities): All money quantities must be positive.')
        else:
            func(self, money_qty)
    return wrapper


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @decorator_validate_positive_quantities
    def add_to_balance(self, money_to_add):
        self.balance += money_to_add
        print(f'-I-: Added \'{money_to_add}\' successfully. Current balance: {self.balance}')
    
    @decorator_validate_positive_quantities
    def retrieve_from_balance(self, money_to_retrieve):
        self.balance -= money_to_retrieve
        print(f'-I-: Retrieved \'{money_to_retrieve}\' successfully. Current balance: {self.balance}')


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance):
        self.min_balance = min_balance
        #BankAccount.__init__(self, balance)
        super().__init__(balance)
    
    def retrieve_from_balance(self, money_to_retrieve):
        try:
            if ((self.balance - money_to_retrieve) < self.min_balance):
                raise InvalidRetrieveOfBalance
        except InvalidRetrieveOfBalance:
            print(f'-E-: Not enough balance to retrieve {money_to_retrieve}.', end=' ')
            print(f'Current balance: {self.balance}. Min balance: {self.min_balance}') 
        else:
            return super().retrieve_from_balance(money_to_retrieve)
    
    def add_to_balance(self, money_to_add):
        return super().add_to_balance(money_to_add)


test_account = SavingsAccount(min_balance=100,balance=150)
test_account.add_to_balance(money_to_add=200)
test_account.retrieve_from_balance(money_to_retrieve=300)
test_account.retrieve_from_balance(money_to_retrieve=-150)