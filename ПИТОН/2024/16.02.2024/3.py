
def only_long_words(func):
    def wrapper(text):
        result = []
        for word in text.split():
            if len(word) > 2:
                result.append(word)
            else:
                print(f"asdjaskjd {word}")
        return func(" ".join(result))
    return wrapper

@only_long_words
def count_words(text):
    return len(text.split())

text = "Все ачв ячслджфыа сс фыволафат сс дывоатыва ии"

print(count_words(text))