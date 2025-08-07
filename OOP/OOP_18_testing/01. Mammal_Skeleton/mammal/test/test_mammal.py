from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("Archy", "Dog", "Bark")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.mammal.name, "Archy")
        self.assertEqual(self.mammal.type, "Dog")
        self.assertEqual(self.mammal.sound, "Bark")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound_returns_correct_string(self):
        self.assertEqual(self.mammal.make_sound(), "Archy makes Bark")

    def test_get_kingdom_returns_correct_string(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info_returns_correct_string(self):
        self.assertEqual(self.mammal.info(), "Archy is of type Dog")

if __name__ == '__main__':
    main()