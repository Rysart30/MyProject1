list_of_words = []
LONG_TEXT = """asdlknfasldkmfasdfasdf"""


def add_word(w: str):
    list_of_words.append(w)
    return list_of_words


def get_words(g: str):
    list_of_words.sort()
    matches = []
    if g == '':
        return list_of_words[:5]
    else:
        for match in list_of_words:
            if g in match:
                matches.append(match)
        return matches[:5]


def crop_text(n: int):
    for i in range(0, len(LONG_TEXT), n):
        yield LONG_TEXT[i:i+n]
