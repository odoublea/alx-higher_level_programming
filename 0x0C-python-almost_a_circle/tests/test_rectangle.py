import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation_id(self):
        """Checks if rectangle is created"""
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.id, 7)

        r2 = Rectangle(8, 9)
        self.assertEqual(r2.id, 8)

        r3 = Rectangle(8, 9, 0, 0, 89)
        self.assertEqual(r3.id, 89)

        r4 = Rectangle(2, 5)
        self.assertEqual(r4.id, 9)


if __name__ == '__main__':
    unittest.main()
