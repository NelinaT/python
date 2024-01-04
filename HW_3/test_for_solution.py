import unittest
from HW_3 import Candy, Person, Kid, Host, biggest_sweet, FluxCapacitor


class TestCandy(unittest.TestCase):
    def test_get_uranium_quantity(self):
        candy = Candy(20, 0.3)
        self.assertEqual(candy.get_uranium_quantity(), 6.0)

    def test_get_mass(self):
        candy = Candy(20, 0.3)
        self.assertEqual(candy.get_mass(), 20)


class TestPerson(unittest.TestCase):
    def test_get_position(self):
        person = Person((1, 2))
        self.assertEqual(person.get_position(), (1, 2))

    def test_set_position(self):
        person = Person((1, 2))
        person.set_position((3, 4))
        self.assertEqual(person.get_position(), (3, 4))


class TestKid(unittest.TestCase):
    def test_add_candy(self):
        kid = Kid((0, 0), 123)
        candy1 = Candy(15, 0.2)
        kid.add_candy(candy1)
        self.assertIn(candy1, kid.candies)

    def test_is_critical(self):
        kid = Kid((0, 0), 123)
        candy1 = Candy(15, 0.2)
        kid.add_candy(candy1)
        self.assertFalse(kid.is_critical())
        candy2 = Candy(10, 2.0)
        kid.add_candy(candy2)
        self.assertTrue(kid.is_critical())


class TestHost(unittest.TestCase):
    def test_remove_candy(self):
        host = Host((3, 4), [(10, 0.5), (15, 0.3), (12, 0.1)])
        candy1 = host.remove_candy(lambda candies: max(candies, key = lambda candy: candy.get_mass()))
        self.assertEqual(candy1.get_mass(), 15)
        candy2 = host.remove_candy(lambda candies: max(candies, key = lambda candy: candy.get_mass()))
        self.assertEqual(candy2.get_mass(), 12)
        candy3 = host.remove_candy(lambda candies: max(candies, key = lambda candy: candy.get_mass()))
        self.assertEqual(candy3.get_mass(), 10)


class TestFluxCapacitor(unittest.TestCase):
    def test_get_victim(self):
        kid1 = Kid((0, 0), 123)
        kid2 = Kid((1, 1), 150)
        host = Host((0, 0), [(10, 0.5)])
        flux_capacitor = FluxCapacitor({kid1, kid2, host})
        victims = flux_capacitor.get_victim()

        if victims is not None:
            self.assertEqual(len(victims), 1)
        else:
            self.assertIsNone(victims)

if __name__ == "__main":
    unittest.main()