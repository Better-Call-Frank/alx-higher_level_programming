#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to be retrieved.
                If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            # If attrs is None, retrieve all attributes
            attrs = ["first_name", "last_name", "age"]

        json_dict = {}
        for attr_name in attrs:
            if hasattr(self, attr_name):
                attr_value = getattr(self, attr_name)
                json_dict[attr_name] = attr_value
        return json_dict
