#!/usr/bin/python3

"""
This module contains unittests for the base.py module.

Unittest classes:
    TestBaseInstantiation - line 21
    TestBaseToJsonString - line 108
    TestBaseSaveToFile - line 154
    TestBaseFromJsonString - line 232
    TestBaseCreate - line 286
    TestBaseLoadFromFile - line 338
    TestBaseSaveToFileCsv - line 404
    TestBaseLoadFromFileCsv - line 482
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing the instantiation of the Base class."""
    
    # Test cases go here...
    
class TestBaseToJsonString(unittest.TestCase):
    """Unittests for testing the to_json_string method of the Base class."""
    
    # Test cases go here...
    
class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing the save_to_file method of the Base class."""
    
    # Test cases go here...
    
class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for testing the from_json_string method of the Base class."""
    
    # Test cases go here...
    
class TestBaseCreate(unittest.TestCase):
    """Unittests for testing the create method of the Base class."""
    
    # Test cases go here...
    
class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for testing the load_from_file method of the Base class."""
    
    # Test cases go here...
    
class TestBaseSaveToFileCsv(unittest.TestCase):
    """Unittests for testing the save_to_file_csv method of the Base class."""
    
    # Test cases go here...
    
class TestBaseLoadFromFileCsv(unittest.TestCase):
    """Unittests for testing the load_from_file_csv method of the Base class."""
    
    # Test cases go here...
    

if __name__ == "__main__":
    unittest.main()
