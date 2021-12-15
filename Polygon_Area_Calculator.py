# "Polygon Area Calculator" by HL
import math

class Rectangle:
    '''This class creates a rectangle object'''
    def __init__(self, width, height):
        '''Initializes the rectangle with a width and height'''
        self.width = width
        self.height = height
    def __str__(self):
        '''Provides a string description of the rectangle object'''
        return 'Rectangle(width=' +str(self.width)+ ', height=' + str(self.height)+')'
    def set_width(self, w):
        '''Set method for rectangle object to set the width.
        Paramters: width as integer
        Returns: new self.width'''
        self.width = w
        return self.width
    def set_height(self, h):
        '''Set method for rectangle object to set the width.
        Paramters: height as integer
        Returns: new self.height'''
        self.height = h
        return self.height
    def get_perimeter(self):
        '''Get method for rectangle object to return perimeter
        Parameters: None
        Returns: calculated perimeter as integer'''
        return (2*self.width+2*self.height)
    def get_area(self):
        '''Get method for rectangle object to return area
        Parameters: None
        Returns: calculated area of rectangle as integer'''
        return (self.width*self.height)
    def get_diagonal(self):
        '''Get method for rectangle object to return diagonal
        Parameters: None
        Returns: calculated diagonal of rectangle as integer'''
        return ((self.width**2 + self.height**2)**.5)
    def get_picture(self):
        '''Get method for rectangle to print out an ascii representation of the rectangle
        Parameters: None
        Returns: an ascii picture of the rectangle'''
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
        '''Calculates how many times rectangle can fit in another shape.
        Parameters: Another rectangle or square object
        Returns: integer calculation'''
        return math.floor(self.get_area()/shape.get_area())

class Square(Rectangle):
    '''Subclass of rectangle class for squares. '''
    def __init__(self, side):
        '''Initializes rectangle with one argument for side to pass to rectangle for both width and height'''
        self.side = side
        super().__init__(side, side)
    def __str__(self):
        '''Provides a string description of the square object'''
        return 'Square(side=' + str(self.side)+')'
    def set_width(self, length):
        '''Overrides rectangles set width method to set both width and height with one side
        Parameters: integer for side to set
        Returns: updated side length for square object'''
        self.side = length
        super().set_width(length)
        super().set_height(length)
        return self.side
    def set_height(self, length):
        '''Overrides rectangles set width method to set both width and height with one side
        Parameters: integer for side to set
        Returns: updated side length for square object'''
        self.side = length
        super().set_width(length)
        super().set_height(length)
        return self.side
    def set_side(self, length):
        '''Set method to set side of rectangle using any length for all sides
        Parameters: integer for side to set
        Returns: updated side length for square object  '''
        self.side = length
        super().set_width(length)
        super().set_height(length)
        return self.side
