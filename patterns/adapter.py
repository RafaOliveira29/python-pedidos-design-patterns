from abc import ABC, abstractmethod
from typing import List
from domain.models import OrderItem


class LegacyShippingService:
    """
    Serviço legado de frete com interface incompatível.

    Ele calcula o frete somente com base no valor total do pedido.
    """

    def calculate(self, amount: float) -> float:
        if amount >= 200:
            return 0.0  # frete grátis
        return 20.0  # frete fixo simples


class ShippingCalculator(ABC):
    """Target: interface esperada pela aplicação."""

    @abstractmethod
    def calculate_shipping(self, items: List[OrderItem]) -> float:
        pass


class LegacyShippingAdapter(ShippingCalculator):
    """
    Adapter: converte a interface do LegacyShippingService
    para a interface ShippingCalculator esperada pela aplicação.
    """

    def __init__(self, legacy_service: LegacyShippingService):
        self.legacy_service = legacy_service

    def calculate_shipping(self, items: List[OrderItem]) -> float:
        total = sum(item.subtotal() for item in items)
        return self.legacy_service.calculate(total)
