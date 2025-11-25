"""
Финальная задача №2
https://stepik.org/lesson/2022462/step/2?unit=2050885

Легенда:
Вы разрабатываете ядро для системы интернет-магазина.
Вам нужно спроектировать классы для товаров и корзины покупок, используя современные и продвинутые подходы ООП в Python.

Техническое задание:
Ваша задача — реализовать три класса: Product, StockError и ShoppingCart.
Шаблон кода ниже содержит полную систему тестов для проверки вашей реализации.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    name: str
    price: float
    stock: int = 0


class StockError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_product(self, product: Product):
        if product.stock > 0:
            self._items.append(product)
        else:
            raise StockError(f"Товар '{product.name}' отсутствует на складе.")

    @property
    def total_price(self):
        return sum(item.price for item in self._items)

    @classmethod
    def from_products(cls, product_list: list):
        obj = cls()
        for product in product_list:
            obj.add_product(product)
        return obj

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"В вашей корзине {len(self)} товаров на сумму {round(self.total_price, 2)} руб."