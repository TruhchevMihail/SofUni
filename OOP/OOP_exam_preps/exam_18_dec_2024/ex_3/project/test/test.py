from project.gallery import Gallery

from unittest import TestCase, main

class GalleryTests(TestCase):
    def test_init_sets_attributes_and_defaults(self):
        g = Gallery("Art123", "Sofia", 150.5)
        self.assertEqual("Art123", g.gallery_name)
        self.assertEqual("Sofia", g.city)
        self.assertEqual(150.5, g.area_sq_m)
        self.assertTrue(g.open_to_public)
        self.assertEqual({}, g.exhibitions)

    def test_gallery_name_validates_alnum_and_strips(self):
        g = Gallery("  Art9  ", "Plovdiv", 50.0)
        self.assertEqual("Art9", g.gallery_name)
        with self.assertRaises(ValueError) as cm:
            g.gallery_name = "Art Gallery"
        self.assertEqual("Gallery name can contain letters and digits only!", str(cm.exception))
        with self.assertRaises(ValueError) as cm2:
            Gallery("Art!@#", "Varna", 10.0)
        self.assertEqual("Gallery name can contain letters and digits only!", str(cm2.exception))

    def test_city_must_start_with_letter(self):
        with self.assertRaises(ValueError) as cm:
            Gallery("Art1", "1City", 20.0)
        self.assertEqual("City name must start with a letter!", str(cm.exception))
        with self.assertRaises(ValueError) as cm2:
            Gallery("Art1", "", 20.0)
        self.assertEqual("City name must start with a letter!", str(cm2.exception))
        g = Gallery("Art1", "Sofia City", 30.0)
        self.assertEqual("Sofia City", g.city)

    def test_area_must_be_positive(self):
        with self.assertRaises(ValueError) as cm:
            Gallery("Art1", "Sofia", 0.0)
        self.assertEqual("Gallery area must be a positive number!", str(cm.exception))
        with self.assertRaises(ValueError) as cm2:
            Gallery("Art1", "Sofia", -5)
        self.assertEqual("Gallery area must be a positive number!", str(cm2.exception))
        g = Gallery("Art1", "Sofia", 1)
        self.assertEqual(1, g.area_sq_m)

    def test_add_exhibition_adds_and_prevents_duplicates(self):
        g = Gallery("Art1", "Sofia", 10)
        msg1 = g.add_exhibition("Impressionism", 2022)
        self.assertEqual('Exhibition "Impressionism" added for the year 2022.', msg1)
        self.assertIn("Impressionism", g.exhibitions)
        self.assertEqual(2022, g.exhibitions["Impressionism"])
        msg2 = g.add_exhibition("Impressionism", 2023)
        self.assertEqual('Exhibition "Impressionism" already exists.', msg2)
        self.assertEqual(2022, g.exhibitions["Impressionism"])

    def test_remove_exhibition_behaviour(self):
        g = Gallery("Art1", "Sofia", 10)
        g.add_exhibition("Modern", 2020)
        g.add_exhibition("Classic", 2018)
        msg_not_found = g.remove_exhibition("Baroque")
        self.assertEqual('Exhibition "Baroque" not found.', msg_not_found)
        msg_removed = g.remove_exhibition("Modern")
        self.assertEqual('Exhibition "Modern" removed.', msg_removed)
        self.assertNotIn("Modern", g.exhibitions)
        self.assertIn("Classic", g.exhibitions)

    def test_list_exhibitions_when_open(self):
        g = Gallery("Art1", "Sofia", 10)
        self.assertEqual("", g.list_exhibitions())
        g.add_exhibition("A", 2001)
        g.add_exhibition("B", 2002)
        expected = "A: 2001\nB: 2002"
        self.assertEqual(expected, g.list_exhibitions())

    def test_list_exhibitions_when_closed(self):
        g = Gallery("  G1  ", "Sofia", 10, open_to_public=False)
        msg = g.list_exhibitions()
        self.assertEqual(
            "Gallery G1 is currently closed for public! Check for updates later on.",
            msg,
        )

if __name__ == '__main__':
    main()