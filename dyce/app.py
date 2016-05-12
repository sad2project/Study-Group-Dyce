from dyce.die import *
from dyce.roller import *
from collections import namedtuple


def numeric(value):
    return str(value)

d6 = Die('d6',
         Face(FaceValue(1, numeric)),
         Face(FaceValue(2, numeric)),
         Face(FaceValue(3, numeric)),
         Face(FaceValue(4, numeric)),
         Face(FaceValue(5, numeric)),
         Face(FaceValue(6, numeric)))

Modifier = namedtuple('Modifier', ['value', 'unit'])

roller = ModifierRoller(MultiRoller(36, BaseRoller(d6)), Modifier(5, numeric))
roll = roller.roll()

print(roller.algorithm_output)
print(roll.intermediate_output)
print(roll.final_output)
