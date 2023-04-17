#!/usr/bin/python3
"""Unittest for square file: class and methods"""


import pep8
import unittest
import sys
from models import square
from models.square import Square
from models.base import Base
from io import StringIO


class Test_Square_outputs(unittest.TestCase):
    """Test_Square_outputs test output for methods
    of Square instances."""
    def test_id_setting(self):
        """test_id_setting method that test the id input"""
        Base._Base__nb_objects = 0

        Sq1 = Square(2)
        self.assertEqual(Sq1.id, 1)
        Sq2 = Square(4)
        self.assertEqual(Sq2.id, 2)
        Sq3 = Square(4, 3, 3, 4)
        self.assertEqual(Sq3.id, 4)
        Sq4 = Square(2)
        self.assertEqual(Sq4.id, 3)
        Sq5 = Square(7, 3, 2, -4)
        self.assertEqual(Sq5.id, -4)

    def test_area_method(self):
        """test_area_method method to test output
        of area method for Square instances"""
        Base._Base__nb_objects = 0
        Sq6 = Square(2)
        self.assertEqual(Sq6.area(), 4)
        Sq7 = Square(6)
        self.assertEqual(Sq7.area(), 36)

    def test_display_method(self):
        """test_display_method method to test output
        of area method for Square instances"""
        Base._Base__nb_objects = 0
        Sq8 = Square(3)
        printed_stream = StringIO()
        sys.stdout = printed_stream
        Sq8.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_stream.getvalue(), "###\n###\n###\n")
        Sq9 = Square(3, 1, 1)
        printed_stream2 = StringIO()
        sys.stdout = printed_stream2
        Sq9.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_stream2.getvalue(), "\n ###\n ###\n ###\n")

    def test_str_method(self):
        """test_str_method to test str output"""
        Base._Base__nb_objects = 0
        Sq12 = Square(6)
        self.assertEqual(Sq12.__str__(), "[Square] (1) 0/0 - 6")
        Sq13 = Square(3, 3, 3, 12)
        self.assertEqual(Sq13.__str__(), "[Square] (12) 3/3 - 3")

    def test_update_method(self):
        """test_update_method to test update instance method"""
        Base._Base__nb_objects = 0
        Sq_up = Square(3, 4, 5)
        # testing *args
        Sq_up.update(3)
        self.assertEqual(Sq_up.__str__(), "[Square] (3) 4/5 - 3")
        Sq_up.update(3, 4)
        self.assertEqual(Sq_up.__str__(), "[Square] (3) 4/5 - 4")
        Sq_up.update(3, 4, 5)
        self.assertEqual(Sq_up.__str__(), "[Square] (3) 5/5 - 4")
        Sq_up.update(3, 4, 5, 6)
        self.assertEqual(Sq_up.__str__(), "[Square] (3) 5/6 - 4")
        # testing **kwargs
        Sq_up.update(id=12)
        self.assertEqual(Sq_up.__str__(), "[Square] (12) 5/6 - 4")
        Sq_up.update(id=12, size=3)
        self.assertEqual(Sq_up.__str__(), "[Square] (12) 5/6 - 3")
        Sq_up.update(id=12, size=3, x=3)
        self.assertEqual(Sq_up.__str__(), "[Square] (12) 3/6 - 3")
        Sq_up.update(id=12, size=3, x=3, y=7)
        self.assertEqual(Sq_up.__str__(), "[Square] (12) 3/7 - 3")

    def test_to_dictionary(self):
        """test_to_dictionary test method output"""
        Base._Base__nb_objects = 0
        S = Square(2, 2, 2, 1)
        out_expect = {'x': 2, 'y': 2, 'size': 2, 'id': 1}
        self.assertEqual(S.to_dictionary(), out_expect)


class TestRaiseExceptions(unittest.TestCase):
    """TestRaiseExceptions test exceptions for Square subclass"""

    def test_not_int_input(self):
        """test_not_int_input method to test not int input
        for size, x, and y attributes"""
        Base._Base__nb_objects = 0
        # size not int
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Sq14 = Square("width", 3, 4)
        # x argument not int
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Sq16 = Square(6, "x", 4)
        # y argument not int
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Sq17 = Square(8, 3, "y")

    def test_input_under_or_equal_0(self):
        """test_input_under_or_equal_0 method that test setter
        validation of width, height, x and y attributes"""
        Base._Base__nb_objects = 0
        # width argument < 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Sq18 = Square(-2, 2, 3, 4)
        # width argument == 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Sq19 = Square(0, 7, 3, 4)
        # x argument < 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Sq22 = Square(6, -3, 3, 4)
        # y argument < 0
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Sq23 = Square(6, 3, -3, 1)


class TestSquarepep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        square = "models/square.py"
        test_square = "tests/test_models/test_square.py"
        result = style.check_files([square, test_square])
        self.assertEqual(result.total_errors, 0)


class TestDocs(unittest.TestCase):
    """test docstrings for square and test_square files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(square.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

