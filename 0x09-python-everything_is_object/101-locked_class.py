#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance attributes,
    except for the attribute 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initialize the 'LockedClass' object with 'first_name' attribute set to None.
        """
        self.first_name = None

    def __setattr__(self, name, value):
        """
        Override the attribute assignment behavior to control the creation of instance attributes.

        Args:
            name (str): The name of the attribute being assigned.
            value (Any): The value to be assigned to the attribute.

        Raises:
            AttributeError: If an attribute other than 'first_name' is being assigned,
                            and 'first_name' attribute is not yet initialized.
        """
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        else:
            super().__setattr__(name, value)
