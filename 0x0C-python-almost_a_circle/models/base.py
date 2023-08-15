#!/usr/bin/python3
"""Defines a Base class for other classes in the project."""


import json
import os
import csv


class Base:
    """Private class attribute: __nb_objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance."""

        if type(id) != int and id is not None:
            raise TypeError("id most be integer")

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file.
        """

        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""

        i = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            i = json.loads(json_string)
        return i

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        i = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    i.append(cls.create(**d))
        return i

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                list_dict = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        list_dict.append({"id": int(row[0]),
                                          "width": int(row[1]),
                                          "height": int(row[2]),
                                          "x": int(row[3]),
                                          "y": int(row[4])})
                    elif cls.__name__ == "Square":
                        list_dict.append({"id": int(row[0]),
                                          "size": int(row[1]),
                                          "x": int(row[2]),
                                          "y": int(row[3])})
                list_inst = []
                for d in list_dict:
                    list_inst.append(cls.create(**d))
                return list_inst
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle window and draws rectangles and squares."""

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle or square."""

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
