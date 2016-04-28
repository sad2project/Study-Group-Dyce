class BaseRoller:
    def __init__(self, die):
        if die is None:
            raise TypeError("Die must not be None.")
        self.die = die

    def roll(self):
        return BaseRoller.BaseResult(self.die.roll())

    class BaseResult:
        def __init__(self, roll):
            if roll is None:
                raise TypeError("Roll must not be None.")
            self.roll = roll

        @property
        def final_output(self):
            return ' | '.join(fv.unit(fv.value) for fv in self.roll.faceValues)

        @property
        def algorithm_output(self):
            return self.roll.die.name