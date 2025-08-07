class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main

class IntegerListTests(TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3)

    def test_init(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_init_takes_only_integers(self):
        list_with_non_integers = IntegerList(1, "2", 3, 4.5)
        self.assertEqual([1, 3], list_with_non_integers.get_data())

    def test_add(self):
        self.list.add(4)
        self.assertEqual([1, 2, 3, 4], self.list.get_data())
        with self.assertRaises(ValueError) as context:
            self.list.add("not an int")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index(self):
        removed_element = self.list.remove_index(0)
        self.assertEqual(1, removed_element)
        self.assertEqual([2, 3], self.list.get_data())

    def test_remove_index_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.list.remove_index(5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get(self):
        self.assertEqual(3, self.list.get(2))
        with self.assertRaises(IndexError) as context:
            self.list.get(3)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert(self):
        self.list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], self.list.get_data())

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.list.insert(5, 5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_non_integer(self):
        with self.assertRaises(ValueError) as context:
            self.list.insert(0, "not an int")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_get_biggest(self):
        self.assertEqual(3, self.list.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.list.get_index(1))
        self.assertEqual(1, self.list.get_index(2))
        self.assertEqual(2, self.list.get_index(3))


if __name__ == '__main__':
    main()