import person

class Director(person.Person):
    __instance = None

    def __new__(cls, gender, full_name, age):
        if not cls.__instance:
            cls.__instance = super(person.Person, cls).__new__(cls)
        return cls.__instance

print()
musk = Director(person)