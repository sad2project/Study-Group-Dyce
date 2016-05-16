from unittest import TestCase
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core import *
from hamcrest.library.object import *
from dyce.roller import *
from dyce.die import *


def unit1(value):
    return '1: ' + str(value)

def unit2(value):
    return '2: ' + str(value)


class BaseRoller_Test(TestCase):
    def setUp(self):
        self.die = Die("Test", 0, 0)

    def test_die_cannot_be_None(self):
        with self.assertRaises(TypeError):
            BaseRoller(None)

    def test_has_given_Die(self):
        roller = BaseRoller(self.die)

        assert_that(roller.die, is_(self.die))

    def test_roll_returns_result(self):
        test = BaseRoller(self.die)

        result = test.roll()

        assert_that(result, instance_of(BaseRoller.BaseResult))


class BaseResult_Test(TestCase):
    def setUp(self):
        self.die = Die("Test",
                       Face(FaceValue(1, unit1)),
                       Face(FaceValue(1, unit1)))
        self.result = BaseRoller(self.die).roll()

    def test_final_output_not_None(self):
        result = self.result.finalOutput

        self.assertIsNotNone(result)

    def test_final_output_is_value_from_unit(self):
        result = self.result.finalOutput

        assert_that(result, equal_to(unit1(1)))

    def test_final_output_works_with_multiple_face_values(self):
        facevalue1 = FaceValue(1, unit1)
        facevalue2 = FaceValue(1, unit2)
        die = Die("Test",
                  Face(facevalue1, facevalue2),
                  Face(facevalue1, facevalue2))
        result = BaseRoller(die).roll()

        test_result = result.finalOutput

        assert_that(test_result, any_of(
            equal_to(unit1(1) + ' | ' + unit2(1)),
            equal_to(unit2(1) + ' | ' + unit1(1))))

    def test_algorithm_output_is_Die_name(self):
        result = self.result.algorithmOutput

        assert_that(result, equal_to(self.die.name))

    def test_intermediate_output_is_not_None(self):
        result = self.result.intermediateOutput

        self.assertIsNotNone(result)

    def test_intermediate_output_is_face_from_die(self):
        facevalue1 = FaceValue(1, unit1)
        facevalue2 = FaceValue(1, unit2)
        die = Die("Test",
                  Face(facevalue1, facevalue2),
                  Face(facevalue1, facevalue2))
        result = BaseRoller(die).roll()

        test_result = result.intermediateOutput

        assert_that(test_result, any_of(
            equal_to('[' + unit1(1) + ' | ' + unit2(1) + ']'),
            equal_to('[' + unit2(1) + ' | ' + unit1(1) + ']')))

# algorithm = 2d6 + 3
# intermediate = [2][5] + 3
# final = 10