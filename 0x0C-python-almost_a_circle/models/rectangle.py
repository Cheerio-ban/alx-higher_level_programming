#!/usr/bin/python3

"""
A Rectangle class that inherits from the Base Class
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle
    Inherited all fields from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle class

        Args:
            width (int): The width of the rectangle class
            height (int): The height of the rectangle class
            x (int): x
            y (int): y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Field width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Field width setter with input validations"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Field height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Field height setter with input validation"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Field x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Field x setter with input validations"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Field y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Field y setter with input validations"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes and returns the area of the
        rectangle class instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using the char '#' in stdout
        """
        for p in range(self.__y):
            print("")
        for i in range(self.__height):
            for q in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        Prints the rectangle to stdout
        Gets called when the print statement is used
        on an instance of the class
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the class instance
        """
        i = 0
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
            Returns a dictionary representation
            of the Rectangle attributes
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
