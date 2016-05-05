class BaseRoller:
    def __init__(self, die):
        if die is None:
            raise TypeError("Die must not be None.")
        self.die = die

    def roll(self):
        return BaseRoller.BaseResult(self.die.roll(), self)

    @property
    def algorithm_output(self):
        return self.die.name

    class BaseResult:
        def __init__(self, roll, roller):
            self.roll = roll
            self.roller = roller

        @property
        def final_output(self):
            return ' | '.join(fv.unit(fv.value) for fv in self.roll.faceValues)

        @property
        def algorithm_output(self):
            return self.roller.algorithm_output

        @property
        def intermediate_output(self):
            return '[' + self.final_output + ']'