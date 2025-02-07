# Class Rectangle

class Rectangle:

    def __init__(self, width, height):
        # Initiation by attributes of the class
        self.width = width
        self.height = height

    def get_square(self):
        # Method of area determination. Method overloading.
        if isinstance(self, Rectangle):         # Validation of belonging to the method.
            return self.width * self.height

    def __eq__(self, other):
        # Method of comparison with the area. Method overloading.
        if isinstance(self, Rectangle) and isinstance(other, Rectangle):
            return self.get_square() == other.get_square()

    def __add__(self, other):
        # Addition method. Method overloading. Designed to add only instances of the Rectangle class.
        width = 1
        height = self.get_square() + other.get_square()
        return Rectangle(width, height)

    def __mul__(self, n):
        # Multiplication method. Method overloading. Designed to multiply an instance of the class by an integer.
        width = self.width * n
        height = self.height
        return Rectangle(width, height)

    def __str__(self):
        return f"Площа прямокутника {self.width}*{self.height} = {Rectangle.get_square(self)} кв.од."


# Validations.
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
print(r1 * 4)
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("Good!")