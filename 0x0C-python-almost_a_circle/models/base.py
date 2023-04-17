#!/usr/bin/python3
"""This module contains a class name Base"""


import json
import os


class Base:
    """This class is the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ constructor method
        Args:
            id ([int], optional): id argument. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method to pass to json string representation
        Args:
            list_dictionaries ([list of dicts]): list of dictionaries
        """
        if list_dictionaries is not [] and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method that writes the json string representation of
        list_obts to a file.
        Args:
            list_objs ([list of objects]): list of cls instances
        """
        list_dicts_python = []
        class_name = cls.__name__ + ".json"
        if list_objs is not None:
            for x in list_objs:
                list_dicts_python.append(x.to_dictionary())
        with open(class_name, "w+", encoding="utf-8") as a_file:
                a_file.write(cls.to_json_string(list_dicts_python))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string method that returns the list
        of the JSON string representation
        Args:
            json_string ([str]): string json representation
        Returns:
            [list]: list of python dictionaries representation
        """
        if json_string is not "" and json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """create method to create an instance from an actual
        instance and update attributes
        Returns:
            [cls instance]: instance of cls
        """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file method that read json file, converts it to python
        and convert each dict into instance of cls class
        Returns:
            [list of instances]: list of cls instances
        """
        list_obj = []
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as js_f:

                list_dict = cls.from_json_string(js_f.read())
                for i in list_dict:
                    list_obj.append(cls.create(**i))
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv save to csv file
        Args:
            list_objs ([list]): list
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".csv", "w+") as my_file:
            my_file.write(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv read from csv file
        Returns:
            [list]: list of objects
        """
        list_obj = []
        if os.path.exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as js_f:

                list_dict = cls.from_json_string(js_f.read())
                for i in list_dict:
                    list_obj.append(cls.create(**i))
        return list_obj

