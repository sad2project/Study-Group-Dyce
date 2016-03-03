
class Die:
    def __init__(self, name, faces):
        if name is None or len(name.strip()) == 0:
            raise TypeError("Name must not be empty")

        self.name = name
        self.faces = faces