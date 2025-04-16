import math

class RegularPolygon:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def area(self):
        if self.num_sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        n = self.num_sides
        s = self.side_length
        return (n * s * s) / (4 * math.tan(math.pi / n))


# Example usage
polygon2 = RegularPolygon(6, 4)  # Hexagon with side length 4
print("Area of the regular polygon:", polygon2.area())  # Output: ~41.57
