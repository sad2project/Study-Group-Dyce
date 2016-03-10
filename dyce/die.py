
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
        return Roll(self)


class Roll:
    def __init__(self, die):
        self.die = die
