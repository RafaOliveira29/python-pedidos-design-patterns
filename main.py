from domain.models import Product, OrderItem
from domain.order import Order
from patterns.strategy import PercentageDiscountStrategy
from patterns.adapter import LegacyShippingService, LegacyShippingAdapter
from patterns.observer import EmailObserver, LogObserver
from patterns.factory_method import PixPaymentCreator


def main() -> None:
    # Produtos de exemplo
    coffee = Product("Café Especial", 35.0)
    mug = Product("Caneca", 25.0)

    # Estratégia de preço (Strategy)
    pricing = PercentageDiscountStrategy(discount_percent=10)

    # Adapter para serviço de frete legado
    legacy_shipping = LegacyShippingService()
    shipping_calculator = LegacyShippingAdapter(legacy_shipping)

    # Cria pedido
    order = Order(pricing_strategy=pricing, shipping_calculator=shipping_calculator)

    # Observers
    order.add_observer(EmailObserver())
    order.add_observer(LogObserver())

    # Adiciona itens
    order.add_item(OrderItem(coffee, 3))
    order.add_item(OrderItem(mug, 2))

    print("\n--- Resumo do pedido ---")
    print(f"Total produtos (com estratégia): R$ {order.total_products():.2f}")
    print(f"Frete (via serviço legado adaptado): R$ {order.shipping_cost():.2f}")
    print(f"Total final: R$ {order.final_total():.2f}\n")

    # Escolha do meio de pagamento usando Factory Method
    print("Escolhendo meio de pagamento (PIX)...\n")
    payment_creator = PixPaymentCreator()
    order.process_order(payment_creator)


if __name__ == "__main__":
    main()
