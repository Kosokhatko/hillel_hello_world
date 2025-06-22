import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        side = math.isqrt(total_area)  # найкраще ціле кореневе наближення
        while total_area % side != 0:
            side -= 1
        new_width = side
        new_height = total_area // side
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        side = math.isqrt(int(new_area))
        while int(new_area) % side != 0:
            side -= 1
        new_width = side
        new_height = int(new_area) // side
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


# Тестування
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("Усі тести пройдено.")
