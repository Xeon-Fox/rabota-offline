

class AbcModel():
    used_words = []
    def __init__(self) -> None:
        pass

    def is_used(self, word):
        if word in self.used_words:
            return True
        else:
            return False

    def add(self, word):
        self.used_words.append(word)

