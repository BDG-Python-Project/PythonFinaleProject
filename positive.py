from character import Base


class Positive(Base):
    def __init__(self, name, age):
        Base.__init__(self, name, age)

    def say_hello(self, person):
        return self.get_name() + ":\n\tՈղջույն \U0001F642, " + person.get_name()
