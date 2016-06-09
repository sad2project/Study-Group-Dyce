import random
from dyce.roller import BaseRoller


class Die:
    '''Represents a rollable die.'''
    def __init__(self, name, *faces):
        '''Constructor

        Arguments:
        name -- A name for the die
        faces -- A list of at least two Face objects, none of which can be None
        '''
        if name is None or len(name.strip()) == 0:
            raise TypeError("Name must not be empty.")

        if faces is None or len(faces) < 2:
            raise TypeError("Faces must be at least two faces.")

        if None in faces:
            raise TypeError("No faces can be None.")

        self.name = name
        self.faces = [*faces]

    @property
    def roller(self):
        return BaseRoller(self)

    def roll(self):
        '''Returns a Roll object representing the result of a roll of this die'''
        return Roll(self)


class Roll:
    '''Represents the result of rolling a single die.'''
    def __init__(self, die):
        '''Constructor

        Arguments:
        die -- A die to roll.
        '''
        self.die = die
        self.face = random.choice(die.faces)

    @property
    def faceValues(self):
        '''The values showing on the die after being rolled'''
        return self.face.faceValues

    @property
    def units(self):
        '''The units in the face resulting face values'''
        return [fv.unit for fv in self.faceValues]


class Face:
    '''Represents one of the faces of a die. A face may have multiple FaceValues.'''
    def __init__(self, *faceValues):
        '''Constructor

        Arguments:
        faceValues -- A variable number of FaceValue objects. Each FaceValue must be unique and not None.
        '''
        if faceValues is None or None in faceValues:
            raise TypeError("Face Values must not be None.")

        if _hasDuplicateUnits(faceValues):
            raise TypeError("Face Value Units must be unique.")

        self.faceValues = [*faceValues]


def _hasDuplicateUnits(faceValues):
    # creates a set of all the Units in the list of Face Values
    #  and compares its count to the number of Face Values
    units = set(map(lambda fv: fv.unit, faceValues))
    return len(units) != len(faceValues)


class FaceValue:
    '''Represents a value that shows on a die’s face. A face value has a value and a unit.'''
    def __init__(self, value, unit):
        '''Constructor

        Arguments:
        value -- A (typically numeric) value representing the magnitude of the FaceValue
        unit -- A Callable object that defines what the FaceValue represents
        '''
        if not callable(unit):
            raise TypeError("Unit must be Callable.")
        if value is None:
            raise TypeError("Value must not be None.")

        self.value = value
        self.unit = unit

    def __eq__(self, other):
        if other is None: return False
        return self.value == other.value and self.unit == other.unit

