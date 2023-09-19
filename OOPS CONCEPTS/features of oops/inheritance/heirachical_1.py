# Base class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

# Subclass 1
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

# Subclass 2
class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length**2

# Subclass 3
class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create instances of the subclasses
circle = Circle("Circle", 5)
square = Square("Square", 4)
triangle = Triangle("Triangle", 3, 6)

# Calculate and print the areas of shapes
print(f"The area of the {circle.name} is {circle.area()}")
print(f"The area of the {square.name} is {square.area()}")
print(f"The area of the {triangle.name} is {triangle.area()}")
