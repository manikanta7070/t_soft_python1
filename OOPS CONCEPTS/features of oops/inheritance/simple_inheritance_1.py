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
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create instances of the subclasses
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

# Calculate and print the areas of shapes
print(f"The area of the {circle.name} is {circle
