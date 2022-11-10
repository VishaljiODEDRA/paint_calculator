import unittest
from paint_calculator import PaintCalculator


class PaintCalculatorTests(unittest.TestCase):
    #testing area of floor
    def test_get_area_of_floor(self):
        self.room1 = PaintCalculator(8, 8, 7)
        self.assertEqual(self.room1.get_area_of_floor(), 64.00)

    #testing area of windows
    def test_area_of_windows(self):
        self.room2 = PaintCalculator(10, 9, 7)
        self.assertEqual(self.room2.get_area_of_windows(), 12.00)

    #testing area of doors
    def test_get_are_of_door(self):
        self.room3 = PaintCalculator(12, 7, 7)
        self.assertEqual(self.room3.get_are_of_door(), 6.00)

    #testing quantity of required paint
    def test_get_required_paint(self):
        self.room4 = PaintCalculator(12, 8, 7)
        self.assertEqual(self.room4.get_required_paint(), 53.64)

    #testing volume of the rooom
    def test_get_volume_of_room(self):
        self.room5 = PaintCalculator(12, 10, 7)
        self.assertEqual(self.room5.get_volume_of_room(), 840.00)


if __name__ == "__main__":
    unittest.main()