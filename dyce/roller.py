# TODO: Make ABC?
class Roller:
    def roll(self):
        raise NotImplementedError()

    @property
    def algorithmOutput(self):
        raise NotImplementedError()


# TODO: Make ABC?
class Result:
    def __init__(self, roller):
        self.roller = roller

    @property
    def units(self):
        raise NotImplementedError()

    # TODO: test
    def hasUnit(self, unit):        # Implemented
        return unit in self.units

    def unitValue(self, unit):
        raise NotImplementedError()

    @property
    def algorithmOutput(self):     # Implemented
        return self.roller.algorithmOutput

    @property
    def intermediateOutput(self):
        raise NotImplementedError()

    @property
    def finalOutput(self):         #Implemented
        return ' | '.join(unit(self.unitValue(unit)) for unit in self.units)


class BaseRoller(Roller):
    def __init__(self, die):
        if die is None:
            raise TypeError("Die must not be None.")
        self.die = die

    def roll(self):
        return BaseRoller.BaseResult(self.die.roll(), self)

    @property
    def algorithmOutput(self):
        return self.die.name

    class BaseResult(Result):
        def __init__(self, roll, roller):
            super().__init__(roller)
            self.roll = roll

        # TODO: test
        @property
        def units(self):
            return set(fv.unit for fv in self.roll.faceValues)

        # TODO: test
        def unitValue(self, unit):
            return [fv.value
                    for fv in self.roll.faceValues
                    if fv.unit == unit][0]
            # TODO: delegate to Roll
            # This method could then look like:
            # return self.roll.unitValue(unit)

        @property
        def intermediateOutput(self):
            return '[' + self.finalOutput + ']'


# TODO: test
class MultiRoller(Roller):
    def __init__(self, numTimes, roller):
        if numTimes < 2:
            raise TypeError("Number of times to roll was less than 2."
                            "Must be at least 2.")
        if roller is None:
            raise TypeError("Roller to roll multiple times must not be None.")
        self.numTimes = numTimes
        self.roller = roller

    def roll(self):
        results = []
        for i in range(self.numTimes):
            results.append(self.roller.roll())
        return MultiRoller.MultiResult(results, self)

    @property
    def algorithmOutput(self):
        return "{n}{base}".format(
                n=self.numTimes,
                base=self.roller.algorithmOutput)

    class MultiResult(Result):
        def __init__(self, results, roller):
            super().__init__(roller)
            self.results = results

        @property
        def units(self):
            units = set()
            for result in self.results:
                units.update(result.units)
            return units

        def unitValue(self, unit):
            return sum(result.unitValue(unit) for result in self.results)

        @property
        def intermediateOutput(self):
            return "".join(result.intermediateOutput for result in self.results)


# TODO: test
class ModifierRoller(Roller):
    """
    Note: Assumes all units in the modifiers collection are guaranteed to be
    rolled by the roller, but not necessarily the other way around.
    """
    def __init__(self, roller, *modifiers):
        self.modifiers = modifiers
        # TODO: check for and reject duplicate units
        self.roller = roller

    def roll(self):
        return ModifierRoller.ModifierResult(self.roller.roll(), self)

    @property
    def algorithmOutput(self):
        return '{base} + {modifiers}'.format(
                base=self.roller.algorithmOutput,
                modifiers=self._modifierOutput())

    def _modifierOutput(self):
        return " | ".join(mod.unit(mod.value) for mod in self.modifiers)

    class ModifierResult(Result):
        def __init__(self, result, roller):
            super().__init__(roller)
            self.result = result
            self.modifiers = roller.modifiers

        @property
        def units(self):
            return self.result.units

        def unitValue(self, unit):
            return self.result.unitValue(unit) + self._modifierValue(unit)

        def _modifierValue(self, unit):
            possible = [mod.value
                        for mod in self.modifiers
                        if mod.unit == unit]
            if len(possible) == 0:
                return 0
            else:
                return possible[0]

        @property
        def intermediateOutput(self):
            return "{base} + {modifiers}".format(
                    base=self.result.intermediateOutput,
                    modifiers=self.roller._modifierOutput())


# TODO: test
class SumRoller(Roller):
    def __init__(self, *rollers):
        self.rollers = rollers

    def roll(self):
        return SumRoller.SumResult(
            [roller.roll() for roller in self.rollers], self)

    @property
    def algorithmOutput(self):
        return " + ".join('(' + roller.algorithmOutput + ')'
                          for roller in self.rollers)

    class SumResult(Result):
        def __init__(self, results, roller):
            super().__init__(roller)
            self.results = results

        @property
        def units(self):
            units = set()
            for result in self.results:
                units.update(result.units)
            return units

        def unitValue(self, unit):
            return sum(*(result.unitValue(unit) for result in self.results))

        def intermediateOutput(self):
            return " + ".join('(' + result.intermediateOutput + ')'
                              for result in self.results)
