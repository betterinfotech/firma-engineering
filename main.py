"""
About:
A program to determine if an xyz co-ordinate lies within a cylinder.
Note: An xyz point on the cylinder surface is not considered inside.

History:
Who          Date        What
Shane Wilson 04-JUL-2024 Initial version

Future 'To do':
1. Subclass Cylinder to create Closed Cylinder if height needed.
2. Consider a FFT algorithm for the distance multiplication which could be slow.
3. Consider float formatting and round.
4. Refactor Pythagoras class for a general distance formula.
5. Validate xyz co-ordinates before passing to distance function.
"""
from dataclasses import dataclass
import math

# A class to model an (x,y) co-ordinate.
@dataclass
class Point():
    x: float
    y: float

# A class to model an (x,y,z) co-ordinate.
@dataclass
class ThreeDimensionalPoint(Point):
    z: float

# A class to model a Circle.
class Circle(Point):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius
    
    # Getters/setters for radius.
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius: float):
        if radius <= 0:
            # Circle must have a radius.
            raise ValueError("Circle must have a radius.")
        self._radius = radius

# A class to model a cylinder. Note this cylinder has no height component
# (i.e. infinite sides) an looks like a circle but is still considered
# # as a different type so it is subclassed from Circle.
class Cylinder(Circle):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

# A class to hold the math routines needed to compare distances between points.
class Pythagoras():  
    # Use the Distance Method between cylinder co-ordinates and any xyz point.
    @staticmethod
    def distance(cylinder: Cylinder, threeDimensionalPoint: ThreeDimensionalPoint) -> float:
        return math.sqrt((threeDimensionalPoint.x - cylinder.x)**2 +
                         (threeDimensionalPoint.y - cylinder.y)**2)

if __name__ == '__main__':
    # Test cases here.
    threeDimensionalPoint = ThreeDimensionalPoint(x=4, y=5, z=16)
    cylinder = Cylinder(x=1, y=2, radius=8)

    if Pythagoras.distance(cylinder, threeDimensionalPoint) < cylinder.radius:  # Exclude xyz on surface.
        print(f'The {threeDimensionalPoint} is INSIDE the cylinder.')
    else:
        print(f'The {threeDimensionalPoint} is OUTSIDE the cylinder.')    
