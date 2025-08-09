from project.legendary_item import LegendaryItem

from unittest import TestCase, main 


class TestLegendaryItem(TestCase):
    def setUp(self):
        self.legendary_item = LegendaryItem("sword", 100,80, 20)
    
    def test_init(self):
        self.assertEqual(self.legendary_item.identifier, "sword")
        self.assertEqual(self.legendary_item.power, 100)
        self.assertEqual(self.legendary_item.durability,80)
        self.assertEqual(self.legendary_item.price,20)

    def test_invalid_identifier_special_chars(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("sw@rd", 100, 80, 20)
        self.assertEqual(str(ex.exception), "Identifier can only contain letters, digits, or hyphens!")

    def test_invalid_identifier_length(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("abc", 100, 80, 20)
        self.assertEqual(str(ex.exception), "Identifier must be at least 4 characters long!")

    def test_invalid_power_negative(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("sword", -1, 80, 20)
        self.assertEqual(str(ex.exception), "Power must be a non-negative integer!")

    def test_invalid_durability_below_range(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("sword", 100, 0, 20)
        self.assertEqual(str(ex.exception), "Durability must be between 1 and 100 inclusive!")

    def test_invalid_durability_above_range(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("sword", 100, 101, 20)
        self.assertEqual(str(ex.exception), "Durability must be between 1 and 100 inclusive!")

    def test_invalid_price_zero(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("sword", 100, 80, 0)
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

    def test_invalid_price_not_multiple_of_ten(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("sword", 100, 80, 25)
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

    def test_is_precious_true(self):
        self.assertTrue(self.legendary_item.is_precious)

    def test_is_precious_false(self):
        item = LegendaryItem("dagger", 49, 80, 20)
        self.assertFalse(item.is_precious)

    def test_enhance(self):
        self.legendary_item.enhance()
        self.assertEqual(self.legendary_item.power, 200)
        self.assertEqual(self.legendary_item.price, 30)
        self.assertEqual(self.legendary_item.durability, 90)

    def test_evaluate_eligible(self):
        result = self.legendary_item.evaluate(70)
        self.assertEqual(result, "sword is eligible.")

    def test_evaluate_not_eligible_low_durability(self):
        result = self.legendary_item.evaluate(90)
        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_not_eligible_not_precious(self):
        item = LegendaryItem("dagger", 49, 80, 20)
        result = item.evaluate(70)
        self.assertEqual(result, "Item not eligible.")


if __name__ == "__main__":
    main()


