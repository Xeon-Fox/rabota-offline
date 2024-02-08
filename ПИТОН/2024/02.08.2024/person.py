class Gender:
    male = "male"
    female = "female"
    non_binary = ""

class Person:
    __first_name: str
    __last_name: str
    __gender: str
    __age: int
    __partner = None

    def __init__(self, gender, full_name, age):
        self.__gender = gender
        self.__age = age
        self.__first_name, self. __last_name= full_name.split()

    @property
    def name(self):
        return f"{self.__first_name} {self.__last_name}"


    def info(self):
        msg = f"Person: {self.__first_name} {self.__last_name}, {self.__gender}, {self.__age} лет🤠"
        if self.__partner:
            msg += f", в браке с {self.__partner.__first_name} {self.__partner.__last_name}"
        return msg

    def __repr__(self):
        return self.info()

    def __add__(self, other):
        return self.marry(other)

    def marry(self, other):
        if self.__partner or other.__partner:
            return
        if self is other:
            return
        if self.__age < 18 or other.__age < 18:
            return
        if self.__gender == other.__gender:
            return
        self.__partner, other.__partner = other, self
        if self.__gender == Gender.female:
            self.__last_name == other.__last_name
        elif other.__gender == Gender.female:
            other.__last_name == self.__last_name 
        print(f"Подразвляем со свадьбой {self.__first_name} {self.__last_name} и {other.__first_name} {other.__last_name}")
    
natasha = Person(Gender.female, "Nataliya Huesosovna", 42)
alexei = Person(Gender.male, "Alexei Shevtzov", 14)
igor = Person(Gender.male, "Igor Link", 16)
vlad = Person("bisexual", "Vlad Kunyakin", 18)
victor = Person("pidoras", "Victor Slidan", 22)
saul = Person(Gender.female, "Saul Goodman", 50)

victor.marry(natasha)
natasha.marry(saul)
vlad.marry(saul)
alexei.marry(igor)
igor.marry(natasha)
saul.marry(victor)


print(natasha.info())
print(igor.info())
print(alexei.info())
print(vlad.info())
print(victor.info())
print(saul.info())

print(str(vlad))
