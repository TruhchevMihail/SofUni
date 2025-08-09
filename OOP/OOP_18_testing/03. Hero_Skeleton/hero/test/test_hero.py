from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("Harry", 4, 40.0, 20.0)

    def test_init_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_init_values(self):
        self.assertEqual(self.hero.username, "Harry")
        self.assertEqual(self.hero.level, 4)
        self.assertEqual(self.hero.health, 40.0)
        self.assertEqual(self.hero.damage, 20.0)

    def test_str_returns_correct_string(self):
        self.assertEqual(str(self.hero), "Hero Harry: 4 lvl\nHealth: 40.0\nDamage: 20.0\n")

    def test_battle_if_names_are_the_same(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_names_are_different(self):
        other_hero = Hero("Hermione", 4, 40.0, 20.0)
        result = self.hero.battle(other_hero)
        self.assertEqual(self.hero.level, 4)
        self.assertEqual(other_hero.level, 4)
        self.assertEqual(self.hero.health, -40.0)
        self.assertEqual(other_hero.health, -40.0)

    def test_battle_if_health_is_zero(self):
        self.hero.health = 0
        other_hero = Hero("Hermione", 4, 40.0, 20.0)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(other_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_is_zero(self):
        self.hero.health = 50.0
        enemy_hero = Hero("Voldemort", 5, 0.0, 25.0)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_result_draw(self):
        self.hero.health = 100.0
        self.hero.level = 5
        enemy_hero = Hero("Voldemort", 5, 100.0, 20.0)

        result = self.hero.battle(enemy_hero)
        
        self.assertEqual("Draw", result)
        self.assertTrue(self.hero.health <= 0)
        self.assertTrue(enemy_hero.health <= 0)

    def test_battle_result_win(self):
        self.hero.health = 100.0
        self.hero.level = 10
        self.hero.damage = 20.0
        enemy_hero = Hero("Voldemort", 1, 50.0, 5.0)
        
        result = self.hero.battle(enemy_hero)
        
        self.assertEqual("You win", result)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 100.0 - enemy_hero.damage * enemy_hero.level + 5)
        self.assertEqual(self.hero.damage, 25.0)
        self.assertTrue(enemy_hero.health <= 0)

    def test_battle_result_lose(self):
        self.hero.health = 50.0
        self.hero.level = 1
        self.hero.damage = 5.0
        enemy_hero = Hero("Voldemort", 10, 100.0, 20.0)
        
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(enemy_hero.level, 11)
        self.assertEqual(enemy_hero.health, 100.0 - self.hero.damage * self.hero.level + 5)
        self.assertEqual(enemy_hero.damage, 25.0)
        self.assertTrue(self.hero.health <= 0)


if __name__ == '__main__':
    main()