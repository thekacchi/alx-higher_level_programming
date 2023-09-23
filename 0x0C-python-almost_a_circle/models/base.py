#!/usr/bin/python3
"""This module defines the base"""
import json
import csv


class Base:
    """This is the definition for the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The init method for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serializes a list of dictionaries into JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of dictionary from json string
        Args: json string rep of list dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects into a json file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.json".format(class_name)

        with open(filename, mode="w") as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_list)
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set, based on a doctionary)"""
        if cls.__name__ == "Rectangle":
            """create dummy Rectangle instance"""
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            """create dummy Square instance"""
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        """apply values"""
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from JDON file"""
        filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(filename, mode="r") as file:
                json_string = file.read()
                dict_list = Base.from_json_string(json_string)
                instance_list = [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            """Return enpty list of file doesn't exist"""
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to CSV file"""
        filename = "{}.csv".format(cls.__name__)

        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a csv file"""
        filename = "{}.csv".format(cls.__name__)
        instance_list = []

        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[4]), int(row[0]))
                        instance_list.append(instance)
                elif cls.__name__ == "Square":
                    for row in reader:
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[0]))
                        instance_list.append(instance)
        except FileNotFoundError:
            """file doesn't exist, retutn rmpty list"""
            pass

        return instance_list
