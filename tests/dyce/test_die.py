from unittest import TestCase
from dyce.die import *


def unit(anum):
    return str(anum)


def unit2(anum):
    return str(anum)


class Die_Test (TestCase):
    def setUp(self):
        self.someName = "Test"
        self.someFaces = [0, 0]

    def test_name_cannot_be_empty(self):
        with self.assertRaises(TypeError):
            Die("", self.someFaces)

    def test_name_cannot_be_whitespace(self):
        with self.assertRaises(TypeError):
            Die(" \t", self.someFaces)

    def test_name_cannot_be_None(self):
        with self.assertRaises(TypeError):
            Die(None, self.someFaces)

    def test_faces_cannot_be_None(self):
        with self.assertRaises(TypeError):
            Die(self.someName, None)

    def test_faces_cannot_be_empty(self):
        with self.assertRaises(TypeError):
            Die(self.someName, [])

    def test_faces_cannot_have_one_face(self):
        with self.assertRaises(TypeError):
            Die(self.someName, [1])

    def test_faces_cannot_contain_None(self):
        with self.assertRaises(TypeError):
            self.someFaces.append(None)
            Die(self.someName, self.someFaces)

    def test_roll_is_not_None(self):
        die = Die(self.someName, *self.someFaces)

        result = die.roll()

        self.assertIsNotNone(result)

    def test_roll_returns_a_Roll_with_die(self):
        die = Die(self.someName, *self.someFaces)

        result = die.roll()

        self.assertEqual(result.die, die)

    def test_roll_returns_a_Roll_with_Face_from_die(self):
        die = Die(self.someName, *self.someFaces)

        result = die.roll()

        self.assertIn(result.face, self.someFaces)


class Face_Test(TestCase):

    def test_FaceValues_cannot_be_None(self):
        with self.assertRaises(TypeError):
            Face(None)

    def test_no_FaceValues_are_None(self):
        with self.assertRaises(TypeError):
            Face(None)

    def test_no_FaceValues_have_the_same_Unit(self):
        fv1 = FaceValue(1, unit)
        fv2 = FaceValue(2, unit)

        with self.assertRaises(TypeError):
            Face(fv1, fv2)

    def test_can_have_empty_face_values(self):
        Face()


class FaceValue_Test(TestCase):

    def test_needs_non_None_value(self):
        with self.assertRaises(TypeError):
            FaceValue(None, unit)

    def test_unit_must_be_callable(self):
        with self.assertRaises(TypeError):
            FaceValue(9001, "")

    def test_equals_similar_face_value(self):
        fv1 = FaceValue(3, unit)
        fv2 = FaceValue(3, unit)

        self.assertEqual(fv1, fv2)

    def test_not_equal_dissimilar_face_value(self):
        fv1 = FaceValue(3, unit)
        fv2 = FaceValue(5, unit)

        self.assertNotEqual(fv1, fv2)

        fv1 = FaceValue(3, unit)
        fv2 = FaceValue(3, unit2)

        self.assertNotEqual(fv1, fv2)

        fv1 = FaceValue(3, unit2)
        fv2 = FaceValue(5, unit)

        self.assertNotEqual(fv1, fv2)


class Roll_Test(TestCase):

    def test_gets_face_values_of_face(self):
        faceValue = FaceValue(3, unit)
        die = Die("Test", Face(faceValue), Face(faceValue))

        roll = Roll(die)

        self.assertEqual(roll.faceValues, [faceValue])

    def test_gets_units_of_face_values(self):
        faceValue = FaceValue(3, unit)
        die = Die("Test", Face(faceValue), Face(faceValue))

        roll = Roll(die)

        self.assertEqual(roll.units, [unit])
