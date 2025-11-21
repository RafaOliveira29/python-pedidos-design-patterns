from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class PixPaymentProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processando pagamento via PIX no valor de R$ {amount:.2f}...")


class CreditCardPaymentProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processando pagamento via Cartão de Crédito no valor de R$ {amount:.2f}...")


class PaymentProcessorCreator(ABC):
    """
    Creator do Factory Method.
    Subclasses definem qual PaymentProcessor concreto será criado.
    """

    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        pass

    def process_payment(self, amount: float) -> None:
        processor = self.create_processor()
        processor.pay(amount)


class PixPaymentCreator(PaymentProcessorCreator):
    def create_processor(self) -> PaymentProcessor:
        return PixPaymentProcessor()


class CreditCardPaymentCreator(PaymentProcessorCreator):
    def create_processor(self) -> PaymentProcessor:
        return CreditCardPaymentProcessor()
