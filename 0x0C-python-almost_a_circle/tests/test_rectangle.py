import unittest
from models import rectangle
from models.rectangle import Rectangle
from models.base import Base

area = Rectangle.area


class TestRectangle(unittest.TestCase):

    """Unittest for the Rectangle class"""

    def test_documentation(self):
        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(area.__doc__) > 0)

    def test_getter_setter(self):
        """Test setter and getter"""
        Base.__nb_objects = 0

        r1 = Rectangle(2, 5)
        self.assertEqual(r1.id, 8)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 9)

        r3 = Rectangle(8, 9, 0, 0, 89)
        self.assertEqual(r3.id, 89)

        r4 = Rectangle(5, 2, 1, 1)
        self.assertEqual(r4.id, 10)

        r5 = Rectangle(9, 6, 20, 23, 10)
        self.assertEqual(r5.id, 10)

        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 9)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 1)

        self.assertEqual(r5.width, 9)
        self.assertEqual(r5.height, 6)
        self.assertEqual(r5.x, 20)
        self.assertEqual(r5.y, 23)

    def test_rectangle_area(self):
        r6 = Rectangle(8, 9)
        r7 = Rectangle(2, 10)
        r8 = Rectangle(9, 6, 20, 23, 10)

        self.assertEqual(r6.area(), 72)
        self.assertEqual(r7.area(), 20)
        self.assertEqual(r8.area(), 54)

    def test_rectangle_str(self):
        r9 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r9.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_rectangle(self):
        r10 = Rectangle(9, 6, 20, 23, 10)
        r10.update(89, 2, 3, 4)
        self.assertEqual((r10.id, r10.width, r10.height, r10.x, r10.y), (89, 2, 3, 4, 23))

        
if __name__ == '__main__':
    unittest.main()
