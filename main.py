import unittest
from numpy import intp
from paint_calculator import PaintCalculator
from paint_calculator_unit_testing import PaintCalculatorTests


def main():
    #prompting user for width, length and height
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    height = float(input("Enter height: "))
    p = PaintCalculator(width, length, height)
    # getting output based on input
    print(
        f'Area of floor (in metre square) = {p.get_area_of_floor():.2f} metre square'
    )
    print(
        f'Quantity of required paint (in litres) = {p.get_required_paint():.2f} litres'
    )
    print(
        f'Volume of room (in cubic metre) = {p.get_volume_of_room():.2f} cubic metre'
    )


if __name__ == "__main__":
    main()
    unittest.main()
