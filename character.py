class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, person):
        return "Բարև, " + person.get_name()
