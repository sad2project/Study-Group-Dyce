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

fibo = Die('fib13',
           Face(FaceValue(1, numeric)),
           Face(FaceValue(2, numeric)),
           Face(FaceValue(3, numeric)),
           Face(FaceValue(5, numeric)),
           Face(FaceValue(8, numeric)),
           Face(FaceValue(13, numeric)))

Modifier = namedtuple('Modifier', ['value', 'unit'])

_3d6plus5 = ModifierRoller(MultiRoller(3, BaseRoller(d6)), Modifier(5, numeric))
_2dfibo = MultiRoller(2, BaseRoller(fibo))
roller = SumRoller(_3d6plus5, _2dfibo)
roll = roller.roll()

print(roller.algorithmOutput)
print(roll.intermediateOutput)
print(roll.finalOutput)
