import numpy
from math import sqrt, acos

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        return numpy.add(self.coordinates, v.coordinates)
        
        #new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]

    def minus(self, v):
        return numpy.subtract(self.coordinates, v.coordinates)

        #new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]

    def scalar(self, multiplier):
        return numpy.multiply(multiplier, self.coordinates)

        #new_coordinates = [multiplier*x for x in self.coordinates]

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def normalized(self):
        return [x/self.magnitude() for x in self.coordinates]

        """
        try:
            magnitude = self.magnitude()
            return self.scalar(1./magnitude)
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
        """

    def dot_product(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle(self, v):
        return acos(self.dot_product(v)/(self.magnitude()*v.magnitude()))