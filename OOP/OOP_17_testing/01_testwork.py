class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main

class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('John', 100, 100)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_decreases_after_work(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.worker.energy, 98)

    def test_worker_energy_is_increased_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_worker_money_is_increased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_get_info_returns_proper_string(self):
        self.assertEqual(self.worker.get_info(), 'John has saved 0 money.')
        self.worker.work()
        self.assertEqual(self.worker.get_info(), 'John has saved 100 money.')

    def test_work_raises_exception_with_zero_energy(self):
        worker = Worker('Test', 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_raises_exception_with_negative_energy(self):
        worker = Worker('Test', 100, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))


if __name__ == '__main__':
    main()