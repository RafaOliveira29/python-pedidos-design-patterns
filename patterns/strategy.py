from abc import ABC, abstractmethod
from typing import List
from domain.models import OrderItem


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_total(self, items: List[OrderItem]) -> float:
        pass


class RegularPricingStrategy(PricingStrategy):
    """Padrão Strategy - estratégia padrão, sem desconto."""

    def calculate_total(self, items: List[OrderItem]) -> float:
        return sum(item.subtotal() for item in items)


class PercentageDiscountStrategy(PricingStrategy):
    """Padrão Strategy - aplica desconto percentual sobre o total."""

    def __init__(self, discount_percent: float):
        self.discount_percent = discount_percent

    def calculate_total(self, items: List[OrderItem]) -> float:
        total = sum(item.subtotal() for item in items)
        discount = total * (self.discount_percent / 100.0)
        return total - discount
