#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base

class Rectangle(Base):
    """
    represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            width - width object
            height - height object
            x - x object
            y - y object
            id - id object inherited
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ width getter """
        return self.__width
    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height
    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x
    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y
    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns area of the rectangle
        """
        return self.__width * self.__height
    
    def display(self):
        """prints the Rectangle instance with the character #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                    print(' ', end="")
            for j in range(self.__width):
                print("#", end="")
            print()
    def __str__(self):
        """
        overriden __str__ method
        """
        return str('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x, self.__y, self.__width, self.__height))
    
    
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id' : self.id, 'width' : self.width, 'height' :  self.height, 'x' : self.x, 'y' : self.y}
    
    
