print("Polygon Area Calculator")
import re
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return 'Rectangle(width=' +str(self.width)+ ', height=' + str(self.height)+')'
    def set_width(self, w):
        self.width = w
        return self.width
    def set_height(self, h):
        self.height = h
        return self.height
    def get_perimeter(self):
        return (2*self.width+2*self.height)
    def get_area(self):
        return (self.width*self.height)
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            box = ''
            for i in range(self.height):
                row = ''
                for j in range(self.width):
                    row = row + '*'
                box = box + row + '\n'
            return box
    def get_amount_inside(self, shape):
        return math.floor(self.get_area()/shape.get_area())



class Square(Rectangle):
        def __init__(self, side):
            self.side = side
            super().__init__(side, side)
        def __str__(self):
            return 'Square(side=' + str(self.side)+')'
        def set_width(self, length):
            self.side = length
            super().set_width(length)
            super().set_height(length)
            return self.side
        def set_height(self, length):
            self.side = length
            super().set_width(length)
            super().set_height(length)
            return self.side
        def set_side(self, length):
            self.side = length
            super().set_width(length)
            super().set_height(length)
            return self.side

x = Rectangle(5,6)
y = Rectangle(3,2)

#testcode
print(x.get_area())
print(x.get_diagonal())
print(x.get_picture())
x.set_width(9)
print(x.get_area())
print(str(x))
print(x.get_picture())
print(y.get_area(),x.get_area())
print(x.get_amount_inside(y))

z = Square(8)
print(z.side)
print(z.get_area())
z.set_width(10)
print(z.side)
z.set_height(6)
print(z.side)
print(str(z))
print(z.get_picture())

sq = Square(5)
print(sq.side)
sq.set_side(2)
print(sq.side)
print(sq.get_picture())
