import math

class Area:
    def rectangle(length, breadth):
        return length * breadth

    def circle(radius):
        return math.pi * radius ** 2

    def triangle(height, base):
        return (height * base) / 2

    def secant_triangle(side_1, side_2, side_3):
        s = (side_2 + side_1 + side_3) / 2
        return math.sqrt(s * (s - side_1) (s - side_2) (s - side_3))

class SolidArea:
    def cube(side):
        return 6 * side ** 3

    def sphere(self, radius):
        return 4*math.pi*radius**2
