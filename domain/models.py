class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, product: 'Product', quantity: int):
        self.product = product
        self.quantity = quantity

    def subtotal(self) -> float:
        return self.product.price * self.quantity
