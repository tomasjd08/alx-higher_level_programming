#!/usr/bin/python3
"""
Square module
"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """
    class for Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            size - size of the object
            x - x object
            y - y object
            id - id object inherited
        """
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """
        overriden __str__ method
        """
        return str("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """size getter"""
        return self.width
    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
         assigns an argument to each attribute
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
    def to_dictionary(self):
        """returns dictionary representation of a Square"""
        return {'id' : self.id, 'size' : self.width, 'x' : self.x, 'y' : self.y}
        

