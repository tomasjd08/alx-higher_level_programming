#!/usr/bin/python3
"""
base module
"""
import json
import os
import csv
import turtle
class Base:
    """
        Implementing Base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        init - initialization
        Args:
            id: object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        """
        returns the dictionary representation of Base
        """
        return self.__dict__
    
    def update(self):
        """
        update
        """
        pass

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dirctionaries
        Args:
            list_dictionaries: dictionary to be converted to JSON string
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - writes the JSON string representation of list_objs to a file
        Args:
            list_objs: list object to be converted to JSON string and stored in a file
        """
        if list_objs is None:
            return "[]"
        else:
            filename = cls.__name__ + ".json"
            obj_dic = [o.to_dictionary() for o in list_objs]
            json_str = cls.to_json_string(obj_dic)
            with open(filename, 'w') as f:
                f.write(json_str)
    
    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - returns the list of the JSON string representation json_string
        Args:
            json_string: JSON string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """
        create - returns an instance with all attributes already set 
        Args:
            dictionary: can be thought of as a double pointer to a dictionary 
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return []
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """
        load_from_file - returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if filename is None:
            return []
        else:
            with open(filename, 'r') as f:
                json_str = f.read()
                obj_dirc = cls.from_json_string(json_str)
                obj_list = [cls.create(**d) for d in obj_dirc]
                return obj_list
            
    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        lst = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        lst.append(i)
        return lst

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles:
            list_squares:
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
