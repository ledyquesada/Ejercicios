#Combinación

from typing import List

class Order:
    def __init__(self):
        self.products = []
        self.delivery_address = ""

    def add_product(self, product):
        self.products.append(product)

    def set_delivery_address(self, address):
        self.delivery_address = address

    def display_info(self):
        print("Order Details:")
        print("Products:")
        for product in self.products:
            print(f"  - {product}")
        print(f"Delivery Address: {self.delivery_address}")

class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_product(self, product):
        self.order.add_product(product)

    def set_delivery_address(self, address):
        self.order.set_delivery_address(address)

    def get_order(self):
        return self.order

# Singleton
class OrderManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.order_builder = OrderBuilder()
        return cls._instance

    def create_order(self):
        return self.order_builder.get_order()

# Uso de Singleton y Builder
order_manager = OrderManager()

# Crear un pedido
order = order_manager.create_order()
order.add_product("Laptop")
order.add_product("Headphones")
order.set_delivery_address("123 Main St, City")

# Mostrar detalles del pedido
order.display_info()

# Intentar crear otra instancia de OrderManager, debería devolver la misma instancia creada anteriormente
another_order_manager = OrderManager()
print(f"Are the instances the same? {order_manager is another_order_manager}")
