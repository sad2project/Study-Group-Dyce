from unittest import TestCase
from dyce.die import Die


class Die_Test (TestCase):
    def test_can_create_with_name_and_faces(self):
        die = Die("a name", [])

        self.assertIsNotNone(die)

    def test_name_cannot_be_empty(self):
        with self.assertRaises(TypeError):
            die = Die("", [])

    def test_name_cannot_be_whitespace(self):
        with self.assertRaises(TypeError):
            die = Die(" \t", [])

    def test_name_cannot_be_None(self):
        with self.assertRaises(TypeError):
            die = Die(None, [])