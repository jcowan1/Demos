import math

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius

r = int(input("Please enter the radius of the circle: "))
obj = Circle(r)
print("The area of the circle is: ", round(obj.area(), 2))
print("The perimeter of the circle is: ", round(obj.perimeter(), 21))