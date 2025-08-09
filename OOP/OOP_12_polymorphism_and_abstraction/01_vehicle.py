from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


# Test code
if __name__ == "__main__":
    # Test Car
    car = Car(20, 5)
    print(f"Car initial fuel: {car.fuel_quantity}")
    car.drive(3)
    print(f"Car fuel after driving 3 km: {car.fuel_quantity}")  # Should decrease by (5 + 0.9) * 3 = 17.7
    car.refuel(10)
    print(f"Car fuel after refueling with 10 liters: {car.fuel_quantity}")  # Should add all 10 liters

    # Test Truck
    truck = Truck(100, 15)
    print(f"Truck initial fuel: {truck.fuel_quantity}")
    truck.drive(5)
    print(f"Truck fuel after driving 5 km: {truck.fuel_quantity}")  # Should decrease by (15 + 1.6) * 5 = 83
    truck.refuel(50)
    print(f"Truck fuel after refueling with 50 liters: {truck.fuel_quantity}")  # Should add 50 * 0.95 = 47.5 liters

    # Test edge case - not enough fuel
    car2 = Car(10, 5)
    print(f"Car2 initial fuel: {car2.fuel_quantity}")
    car2.drive(2)  # Needs (5 + 0.9) * 2 = 11.8 fuel, which is more than available
    print(f"Car2 fuel after attempting to drive 2 km: {car2.fuel_quantity}")  # Should remain unchanged