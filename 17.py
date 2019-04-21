"""
Q17
Class CreditCard :
 Fields:  balance limit  customer account  bank
Behaviors: make payment(amount) get customer( ) get bank( ) get account( ), get balance( ) get limit( ) charge(price)

Implement Class for CreditCard and document it


Create class PredatoryCreditCard
fields: apr (annual percentage rate)
behavoours : charge(price)
"""


class CreditCard:
    def __init__(self,balancelimit,cusAccountBank):
        self.BL=balancelimit
        self.CAB=cusAccountBank

    def make_payment(self,amount):
        self.amount = amount

    def get_custoomer(self):
        pass

    def get_bank(self):
        print("Account No.",self.CAB)

    def get_account(self):
        pass

    def get_limit(self):
        pass

    def charge(self,price):
        self.price = price
        print("Fine Charge price :",self.price)


CreditCard  = CreditCard(50000, "1D16732")
print(CreditCard.get_bank())


class PredatoryCreditCard:
    def __init__(self,apr):
        self.annual=apr

    def display(self):
        print("apr = ",self.annual)


PredatoryCreditCard = PredatoryCreditCard(3)
print(PredatoryCreditCard.display())







