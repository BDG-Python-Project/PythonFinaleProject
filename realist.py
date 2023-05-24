from character import Base


class Realist(Base):
    def __init__(self, name, age):
        Base.__init__(self, name, age)

    def say_hello(self, person):
        if person.get_age() <= 30:
            content = self.get_name() + ":\n\tԲարև, " + person.get_name() + "!"
        else:
            content = self.get_name() + ":\n\tՈղջուն, " + person.get_name()
        return content
