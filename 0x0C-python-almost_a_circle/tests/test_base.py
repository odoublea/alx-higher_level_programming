import unittest
from models import base
from models.base import Base
Base = Base


class TestBase(unittest.TestCase):
    def test_documentation(self):
        """Test documentation"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_base_creation(self):
        """test base create"""
        a = Base()
        self.assertTrue(isinstance(a, Base))

    def test_instanceID(self):
        """Check if instance initiated and number of
        __nb_instance increases."""

        a1 = Base()
        self.assertEqual(a1.id, 2)
        a2 = Base()
        self.assertEqual(a2.id, 3)
        a3 = Base()
        self.assertEqual(a3.id, 4)
        a4 = Base()
        self.assertEqual(a4.id, 5)
        a5 = Base(56)
        self.assertEqual(a5.id, 56)
        a6 = Base()
        self.assertEqual(a6.id, 6)
        a7 = Base()
        self.assertEqual(a7.id, 7)

    def test_instanceValue(self):
        """Checks the Type of Id"""
        a8 = Base('a')
        self.assertRaises(TypeError, a8.id)


if __name__ == '__main__':
    unittest.main()
