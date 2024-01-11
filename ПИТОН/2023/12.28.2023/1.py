def shorten_word(word: str="") -> str:
    if not type(word) is str:
        return ""
    if len(word) <= 6:
        return word 
    result = word[:3] + '-' + word[-3:]
    return result

def shorten(text="") -> str:
    if not type(text) is str:
        return ""
    result = []
    for word in text.split(" "):
        result.append(shorten_word(word))
    return " ".join(result)

def text_shorten():
    assert shorten("дезоморфин") == "дез-фин"
    assert shorten("метамфетамин") == "мет-мин"
    assert shorten("опа") == "опа"
    assert shorten("") == ""
    assert shorten(75) == ""
    assert shorten() == ""
    assert shorten("опиойд психаделик") == "опиойд пси-лик"
    print("все норм я под солями")

text_shorten()