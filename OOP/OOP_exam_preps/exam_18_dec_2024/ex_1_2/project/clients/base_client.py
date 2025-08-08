from abc import ABC, abstractmethod
import math


class BaseClient(ABC):
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.discount: float = 0.0
        self.total_orders: int = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Name must be at least two characters long!")
        self._name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not isinstance(value, str) or not value.isdigit():
            raise ValueError("Phone number can contain only digits!")
        self._phone_number = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self) -> str:
        discount_percent = math.floor(self.discount)
        return f"Client: {self.name}, Phone number: {self.phone_number}, Orders count: {self.total_orders}, Discount: {discount_percent}%"