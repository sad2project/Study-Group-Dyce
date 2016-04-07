import random


class Die:
    def __init__(self, name, faces):
        if name is None or len(name.strip()) == 0:
            raise TypeError("Name must not be empty.")

        if faces is None or len(faces) < 2:
            raise TypeError("Faces must be at least two faces.")

        if None in faces:
            raise TypeError("No faces can be None.")

        self.name = name
        self.faces = faces

    def roll(self):
        return Roll(self, random.choice(self.faces))


class Roll:
    def __init__(self, die, face):
        self.die = die
        self.face = face


class Face:
    def __init__(self, faceValues):
        if faceValues is None or None in faceValues:
            raise TypeError("Face Values must not be None.")

        if _hasDuplicateUnits(faceValues):
            raise TypeError("Face Value Units must be unique.")

        self.faceValues = faceValues


def _hasDuplicateUnits(faceValues):
    # creates a set of all the Units in the list of Face Values
    #  and compares its count to the number of Face Values
    units = set(map(lambda fv: fv.unit, faceValues))
    return len(units) != len(faceValues)


class FaceValue:
    def __init__(self, unit):
        self.unit = unit