from character import Base


class Fool(Base):
    def __init__(self, name, age):
        Base.__init__(self, name, age)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def say_hello(self, person):
        return self.get_name() + ":\n\tԲարև, " + person.get_name() + "!"
