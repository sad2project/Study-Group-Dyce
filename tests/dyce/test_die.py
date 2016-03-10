from unittest import TestCase
from dyce.die import Die


class Die_Test (TestCase):
    def setUp(self):
        self.someName = "Test"
        self.someFaces = [0, 0]

    def test_can_create_with_name_and_faces(self):
        die = Die(self.someName, self.someFaces)

        self.assertIsNotNone(die)

    def test_name_cannot_be_empty(self):
        with self.assertRaises(TypeError):
            die = Die("", self.someFaces)

    def test_name_cannot_be_whitespace(self):
        with self.assertRaises(TypeError):
            die = Die(" \t", self.someFaces)

    def test_name_cannot_be_None(self):
        with self.assertRaises(TypeError):
            die = Die(None, self.someFaces)

    def test_faces_cannot_be_None(self):
        with self.assertRaises(TypeError):
            die = Die(self.someName, None)

    def test_faces_cannot_be_empty(self):
        with self.assertRaises(TypeError):
            die = Die(self.someName, [])

    def test_faces_cannot_have_one_face(self):
        with self.assertRaises(TypeError):
            die = Die(self.someName, [1])

    def test_faces_cannot_contain_None(self):
        with self.assertRaises(TypeError):
            self.someFaces.append(None)
            die = Die(self.someName, self.someFaces)

    def test_roll_is_not_None(self):
        die = Die(self.someName, self.someFaces)

        result = die.roll()

        self.assertIsNotNone(result)

    def test_roll_returns_a_Roll_with_die(self):
        die = Die(self.someName, self.someFaces)

        result = die.roll()

        self.assertEqual(result.die, die)

