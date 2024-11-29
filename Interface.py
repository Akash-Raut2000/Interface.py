from abc import ABC, abstractmethod

# Interface
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Classes
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."

# Using the interface
payments = [CreditCardPayment(), PayPalPayment()]
for payment in payments:
    print(payment.pay(100))
