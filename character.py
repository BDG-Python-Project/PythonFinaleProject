class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def say_hello(self, person):
        return "Բարև, " + person.get_name()
