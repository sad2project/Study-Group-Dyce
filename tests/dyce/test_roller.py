from unittest import TestCase
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core import *
from hamcrest.library.object import *
from dyce.roller import *
from dyce.die import *


class BaseRoller_Test(TestCase):
    def setUp(self):
        self.die = Die("Test", [0, 0])

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

    def test_roll_cannot_be_None(self):
        with self.assertRaises(TypeError):
            BaseRoller.BaseResult(None)