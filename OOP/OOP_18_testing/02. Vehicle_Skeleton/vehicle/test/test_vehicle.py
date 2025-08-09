from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 150)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.horse_power, 150)
        self.assertEqual(self.vehicle.capacity, 50)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_decreases_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_refuel_with_enough_fuel_increases_fuel(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 35)

    def test_refuel_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_returns_correct_string(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 150 horse power with 50 fuel left and 1.25 fuel consumption")

    def test_fuel_consumption_returns_correct_value(self):
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        
    def test_default_fuel_consumption_class_attribute(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)
        
    def test_init_sets_fuel_to_capacity(self):
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        
    def test_drive_with_exact_fuel_needed(self):

        kilometers = self.vehicle.fuel / self.vehicle.fuel_consumption
        self.vehicle.drive(kilometers)
        self.assertEqual(self.vehicle.fuel, 0)

if __name__ == '__main__':
    main()