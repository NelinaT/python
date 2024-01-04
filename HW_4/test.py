import unittest
from  hw_4 import Potion, ГоспожатаПоХимия
import copy


class Target:
    """Test target."""

    def __init__(self, **kwargs):
        """Initializator."""
        self._cache = kwargs
        for key, val in kwargs.items():
            setattr(self, key, val)
    
    def _refresh(self):
        """Refresh all values to their initial state."""
        for key, val in self._cache.items():
            setattr(self, key, val)


def int_attr_fun(target):
    """Test function for altering int attribute."""
    target.int_attr *= 10


def float_attr_fun(target):
    """Test function for altering float attribute."""
    target.float_attr += 1


def list_attr_fun(target):
    """Test function for altering list attribute."""
    target.list_attr.append(4)


def dict_attr_fun(target):
    """Test function for altering dict attribute."""
    target.dict_attr = {val:key for key, val in target.dict_attr.items()}


class TestBasicPotion(unittest.TestCase):
    """Test Potion class for basic functionality."""

    def setUp(self):
        """Set up a test target."""
        self._target = Target(int_attr=5, float_attr=3.14,
                              list_attr=[1, 2, 3],
                              dict_attr={'name': 'Борис', 'професия': 'жалбар'})

    def test_empty(self):
        """Test initialization with empty effects."""
        potion = Potion({}, duration=0)
        self.assertIsInstance(potion, Potion)

    def test_applying(self):
        """Test applying a potion to a target."""
        potion = Potion({'int_attr_fun': int_attr_fun,
                         'float_attr_fun': float_attr_fun,
                         'list_attr_fun': list_attr_fun,
                         'dict_attr_fun': dict_attr_fun},
                        duration=1)
        potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        potion.float_attr_fun(self._target)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        potion.list_attr_fun(self._target)
        self.assertEqual(self._target.list_attr, [1, 2, 3, 4])
        potion.dict_attr_fun(self._target)
        self.assertEqual(self._target.dict_attr, {'Борис': 'name', 'жалбар': 'професия'})

    def test_depletion(self):
        """Test depletion of a potion effect."""
        potion = Potion({'int_attr_fun': int_attr_fun},
                        duration=2)
        potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        with self.assertRaisesRegex(TypeError, 'Effect is depleted\.'):
            potion.int_attr_fun(self._target)
 

class TestPotionOperations(unittest.TestCase):
    """Test operations for Potion class."""

    def setUp(self):
        """Set up a test target."""
        self._target = Target(int_attr=5, float_attr=3.14)

    def test_combination_no_overlap(self):
        """Test combining potions with no overlap."""
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'float_attr_fun': float_attr_fun}, duration=2)
        potion = potion1 + potion2
        potion.int_attr_fun(self._target)
        potion.float_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        self.assertAlmostEqual(self._target.float_attr, 4.14)

    def test_combination_with_overlap(self):
        """Test combining potions with overlap."""
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=2)
        potion = potion1 + potion2
        potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 500)

    def test_potentiation(self):
        """Test potentiation of a potion."""
        potion = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion = potion * 3
        potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5 * (10 ** 3))

    def test_dilution(self):
        """Test dilution of a potion."""
        # Test at half
        base_potion = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        half_potion = base_potion * 0.5
        half_potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5)
        # Test above half
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        base_potion = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        half_potion = base_potion * 0.51
        half_potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        # Test below half
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        base_potion = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        half_potion = base_potion * 0.49
        half_potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5)
        # Test around zero
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        base_potion = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        half_potion = base_potion * 0.0001
        half_potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5)
        # Test actual division
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        base_potion = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        half_potion = base_potion * 0.5
        half_potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        # Test rounding to odd number (built-in round() always goes to an even number)
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        base_potion = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 3
        half_potion = base_potion * 0.5
        half_potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)

    def test_purification(self):
        """Test purification of a potion."""
        # Test normal behaviour
        potion1 = Potion({'int_attr_fun': int_attr_fun,
                          'float_attr_fun': float_attr_fun},
                         duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun},
                         duration=1)
        potion = potion1 - potion2
        potion.float_attr_fun(self._target)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        with self.assertRaises(AttributeError):
            potion.int_attr_fun(self._target)
        # Test mismatching effects
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion1 = Potion({'int_attr_fun': int_attr_fun,
                          'float_attr_fun': float_attr_fun},
                         duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun},
                         duration=1)
        with self.assertRaises(TypeError):
            potion2 - potion1
        # Test with intensity
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 3
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion_decorator =  Potion({'float_attr_fun': float_attr_fun}, duration=1)
        potion1 = potion1 + potion_decorator
        potion = potion1 - potion2
        potion.float_attr_fun(self._target)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        potion.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        # Test with intensity resulting in zero
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion = potion1 - potion2
        with self.assertRaises(AttributeError):
            potion.int_attr_fun(self._target)
        # Test with higher intensity on the right
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 3
        potion = potion1 - potion2
        with self.assertRaises(AttributeError):
            potion.int_attr_fun(self._target)

    def test_separation(self):
        """Test separation of a potion."""
        # Test normal case
        potion = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 9
        potion1, potion2, potion3 = potion / 3
        potion1.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5 * (10 ** 3))
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion2.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5 * (10 ** 3))
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion3.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 5 * (10 ** 3))
        # Test resulting in one
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 3
        potion1, potion2, potion3 = potion / 3
        potion1.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion2.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion3.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        # Test rounding to odd
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 3
        potion1, potion2 = potion / 2
        potion1.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion2.int_attr_fun(self._target)
        self.assertEqual(self._target.int_attr, 50)

    def test_deprecation(self):
        """Test deprecation of a potion."""
        # Addition
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion = potion1 + potion2
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            potion1.int_attr_fun(self._target)
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            potion2.int_attr_fun(self._target)
        # Multiplication
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion = potion1 * 2
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            potion1.int_attr_fun(self._target)
        # Subtraction
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion = potion1 - potion2
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            potion1.int_attr_fun(self._target)
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            potion2.int_attr_fun(self._target)
        # Division
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion = potion1 / 1
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            potion1.int_attr_fun(self._target)


class TestPotionComparison(unittest.TestCase):
    """Test comparisons for Potion class."""

    def test_equal(self):
        """Test equality of potions."""
        # Normal case
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'float_attr_fun': float_attr_fun}, duration=1)
        potion3 = Potion({'int_attr_fun': int_attr_fun,
                          'float_attr_fun': float_attr_fun},
                         duration=1)
        self.assertEqual(potion1 + potion2, potion3)
        # With intensity
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion3 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion4 = potion1 + potion2
        self.assertEqual(potion4, potion3)
        # Not equal due to different methods
        potion1 = Potion({'float_attr_fun': float_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun,
                          'float_attr_fun': float_attr_fun},
                         duration=1)
        self.assertNotEqual(potion1, potion2)
        # Not equal due to different intensity
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion3 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 3
        potion4 = potion1 + potion2
        self.assertNotEqual(potion4, potion3)

    def test_superbness(self):
        """Test superbness of potions."""
        # Normal case
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        self.assertLess(potion1, potion2)
        self.assertGreater(potion2, potion1)
        self.assertNotEqual(potion1, potion2)
        # Diffetent intensity for different methods
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion2 = Potion({'float_attr_fun': float_attr_fun}, duration=1) * 3
        self.assertLess(potion1, potion2)
        self.assertGreater(potion2, potion1)
        self.assertNotEqual(potion1, potion2)
        # Equal intensity for different methods
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion2 = Potion({'float_attr_fun': float_attr_fun}, duration=1) * 2
        self.assertFalse(potion1 > potion2)
        self.assertFalse(potion1 < potion2)


class TestГоспожатаПоХимия(unittest.TestCase):
    """Test ГоспожатаПоХимия."""

    def setUp(self):
        """Set up a test target."""
        self._target = Target(int_attr=5, float_attr=3.14,
                              list_attr=[1, 2, 3],
                              dict_attr={'name': 'Борис', 'професия': 'жалбар'})
        self._dimitrichka = ГоспожатаПоХимия()
    
    def test_applying_normal_case(self):
        """Test applying a normal potion."""
        potion = Potion({'int_attr_fun': int_attr_fun,
                         'float_attr_fun': float_attr_fun,
                         'list_attr_fun': list_attr_fun,
                         'dict_attr_fun': dict_attr_fun},
                        duration=1)
        self._dimitrichka.apply(self._target, potion)
        self.assertEqual(self._target.int_attr, 50)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        self.assertEqual(self._target.list_attr, [1, 2, 3, 4])
        self.assertEqual(self._target.dict_attr, {'Борис': 'name', 'жалбар': 'професия'})
    
    def test_applying_part_of_potion(self):
        """Test applying only a part of a potion."""
        potion = Potion({'int_attr_fun': int_attr_fun,
                         'float_attr_fun': float_attr_fun,
                         'list_attr_fun': list_attr_fun,
                         'dict_attr_fun': dict_attr_fun},
                        duration=1)
        temp_target = Target(int_attr=5)
        potion.int_attr_fun(temp_target)
        self._dimitrichka.apply(self._target, potion)
        self.assertEqual(self._target.int_attr, 5) # This should be the original value
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        self.assertEqual(self._target.list_attr, [1, 2, 3, 4])
        self.assertEqual(self._target.dict_attr, {'Борис': 'name', 'жалбар': 'професия'})

    def test_applying_depleted_potion(self):
        """Test applying a depleted potion or a potion that was used in a reaction."""
        # Apply a depleted potion
        potion = Potion({'int_attr_fun': int_attr_fun,
                         'float_attr_fun': float_attr_fun,
                         'list_attr_fun': list_attr_fun,
                         'dict_attr_fun': dict_attr_fun},
                        duration=1)
        self._dimitrichka.apply(self._target, potion)
        with self.assertRaisesRegex(TypeError, 'Potion is depleted\.'):
            self._dimitrichka.apply(self._target, potion)
        with self.assertRaisesRegex(TypeError, 'Potion is depleted\.'):
            potion = potion * 2
        # Apply a potion that was used in a reaction
        potion = Potion({'int_attr_fun': int_attr_fun,
                         'float_attr_fun': float_attr_fun,
                         'list_attr_fun': list_attr_fun,
                         'dict_attr_fun': dict_attr_fun},
                        duration=1)
        _ = potion * 2
        with self.assertRaisesRegex(TypeError, 'Potion is now part of something bigger than itself\.'):
            self._dimitrichka.apply(self._target, potion)

    def test_applying_order(self):
        """Test applying order of a potion."""
        # aa_name should have precedence
        def z_name(target):
            target.int_attr += 2
        def aa_name(target):
            target.int_attr *= 2
        potion = Potion({'z_name': z_name,
                         'aa_name': aa_name},
                        duration=1)
        self._dimitrichka.apply(self._target, potion)
        self.assertEqual(self._target.int_attr, 12)
        # z_name should have precedence
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        def z_name(target):
            target.int_attr += 2
        def a_name(target):
            target.int_attr *= 2
        potion = Potion({'z_name': z_name,
                         'a_name': a_name},
                        duration=1)
        self._dimitrichka.apply(self._target, potion)
        self.assertEqual(self._target.int_attr, 14)

    def test_ticking_immutable(self):
        """Test ticking after applying a potion with immutable attributes."""
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=2)
        potion = potion1 + potion2 # Excepted duration is 2 with intensity of 2
        self._dimitrichka.apply(self._target, potion)
        self.assertEqual(self._target.int_attr, 500)
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 500)
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 5)

    def test_ticking_mutable(self):
        """Test ticking after applying a potion with mutable attributes."""
        potion = Potion({'int_attr_fun': int_attr_fun,
                         'float_attr_fun': float_attr_fun,
                         'list_attr_fun': list_attr_fun,
                         'dict_attr_fun': dict_attr_fun},
                        duration=1)
        self._dimitrichka.apply(self._target, potion)
        self.assertEqual(self._target.int_attr, 50)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        self.assertEqual(self._target.list_attr, [1, 2, 3, 4])
        self.assertEqual(self._target.dict_attr, {'Борис': 'name', 'жалбар': 'професия'})
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 5)
        self.assertAlmostEqual(self._target.float_attr, 3.14)
        self.assertEqual(self._target.list_attr, [1, 2, 3])
        self.assertEqual(self._target.dict_attr, {'name': 'Борис', 'професия': 'жалбар'})

    def test_ticking_multiple_potions(self):
        """Test ticking after applying multiple potions which affect the same attribute."""
        # Same attribute
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=2)
        self._dimitrichka.apply(self._target, potion1)
        self._dimitrichka.apply(self._target, potion2)
        self.assertEqual(self._target.int_attr, 500)
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 50)
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 5)
        # Different attributes
        self._target = copy.deepcopy(self._target)
        self._target._refresh()
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1)
        potion2 = Potion({'float_attr_fun': float_attr_fun}, duration=2)
        self._dimitrichka.apply(self._target, potion1)
        self._dimitrichka.apply(self._target, potion2)
        self.assertEqual(self._target.int_attr, 50)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 5)
        self.assertAlmostEqual(self._target.float_attr, 4.14)
        self._dimitrichka.tick()
        self.assertEqual(self._target.int_attr, 5)
        self.assertAlmostEqual(self._target.float_attr, 3.14)

    def test_ticking_multiple_targets(self):
        """Test ticking after applying a potion with mutable attributes."""
        potion1 = Potion({'int_attr_fun': int_attr_fun}, duration=1) * 2
        potion2 = Potion({'int_attr_fun': int_attr_fun}, duration=2)
        target1 = self._target
        target2 = Target(int_attr=5, float_attr=3.14,
                         list_attr=[1, 2, 3],
                         dict_attr={'name': 'Борис', 'професия': 'жалбар'})
        self._dimitrichka.apply(target1, potion1)
        self._dimitrichka.apply(target2, potion2)
        self.assertEqual(target1.int_attr, 500)
        self.assertEqual(target2.int_attr, 50)
        self._dimitrichka.tick()
        self.assertEqual(target1.int_attr, 5)
        self.assertEqual(target2.int_attr, 50)
        self._dimitrichka.tick()
        self.assertEqual(target1.int_attr, 5)
        self.assertEqual(target2.int_attr, 5)


 

if __name__ == '__main__':
    unittest.main()