from character import Base


class Fool(Base):
    def __init__(self, name, age):
        Base.__init__(self, name, age)

    def say_hello(self, person):
        return self.get_name() + ":\n\tԲարև \U0001f600, " + person.get_name() + "!"
