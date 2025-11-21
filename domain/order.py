from typing import List
from domain.models import OrderItem
from patterns.strategy import PricingStrategy
from patterns.adapter import ShippingCalculator
from patterns.observer import OrderObserver


class Order:
    """
    Representa um pedido simples.
    Aplica Strategy para preço, Observer para eventos
    e usa Adapter + Factory Method no fluxo de pagamento.
    """

    def __init__(self, pricing_strategy: PricingStrategy, shipping_calculator: ShippingCalculator):
        self.items: List[OrderItem] = []
        self.pricing_strategy = pricing_strategy
        self.shipping_calculator = shipping_calculator
        self.observers: List[OrderObserver] = []

    # Métodos do padrão Observer
    def add_observer(self, observer: OrderObserver) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)

    # Regras de pedido
    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)
        self.notify_observers(f"Item adicionado: {item.product.name} (x{item.quantity}).")

    def total_products(self) -> float:
        return self.pricing_strategy.calculate_total(self.items)

    def shipping_cost(self) -> float:
        return self.shipping_calculator.calculate_shipping(self.items)

    def final_total(self) -> float:
        return self.total_products() + self.shipping_cost()

    def process_order(self, payment_creator) -> None:
        from patterns.factory_method import PaymentProcessorCreator  # type: ignore

        if not isinstance(payment_creator, PaymentProcessorCreator):
            raise TypeError("payment_creator deve ser uma instância de PaymentProcessorCreator.")

        self.notify_observers("Processando pedido...")
        total = self.final_total()
        payment_creator.process_payment(total)
        self.notify_observers(f"Pedido pago com sucesso. Valor final: R$ {total:.2f}.")
