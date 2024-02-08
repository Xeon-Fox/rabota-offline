class Fly:
    speed = 1
    __phrase = "бззз"

    def __init__(self, speed, phrase):
        self.speed = speed
        self.__phrase = phrase
        
    def say(self):
        return self.__phrase

    def fly(self, distance):
        time = distance // self.speed
        return f"муха пролетела {distance}м за {time}"

class Dog:
    __phrase = "гав"
    speed = 1

    def __init__(self,speed, phrase):
        self.__phrase = phrase

    def say(self):
        return self.__phrase

    def catch(self, smth):
        print(f"собака словила {smth}")

class Flydog(Fly, Dog):
    def __init__(self, speed, phrase):
        super(Fly, self).__init__(speed, phrase)
        super(Dog, self).__init__(speed, phrase)

    def say(self):
        return super(Dog, self).say() + super(Fly, self).say()


fl = Flydog(1, "hi")
Flydog.say()