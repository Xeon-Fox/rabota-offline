

class AbcView():
    def __init__(self) -> None:
        pass

    def show(self, text):
        print(text)

    def show_word(self, word):
        print(f"Cлово оппонента: {word}")

    def show_win(self):
        print("Вы победили урааа")

    def show_loose(self):
        print("Вы проиграли😭")

    def show_mistake(self, first_letter, attempts_left):
        print(f"Слово неправильно, оно должно начанаться с {first_letter}, у вас осталось {attempts_left} попыток")
    
    def show_duplicate(self, attempts_left):
        print(f"Вы уже использовали это слово, попыток осталось: {attempts_left}")

    def show_used(self, word):
        print(f"{word} уже было использовано")

    def show_unknown(self):
        print("Данного слова не сущетсвует")

    def ask_word(self):
        word = input("Ваше слово: ")
        return word

