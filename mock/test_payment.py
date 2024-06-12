import unittest
from unittest.mock import Mock

class PaymentProcessor:
    def process_payment(self, amount):
        pass  # Placeholder implementation for now

class Order:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        self.payment_processor.process_payment(amount)
        return "Payment processed"

class TestOrder(unittest.TestCase):
    def test_checkout(self):
        payment_processor_mock = Mock()
        order = Order(payment_processor_mock)

        result = order.checkout(100)

        self.assertEqual(result, "Payment processed")
        payment_processor_mock.process_payment.assert_called_once_with(100)

if __name__ == '__main__':
    unittest.main()
