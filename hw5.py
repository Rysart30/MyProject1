def flatten(arr):
    for item in arr:
        if isinstance(item, list):
            for subitem in item:
                yield subitem
        else:
            yield item


def grep(pattern):
    while True:
        line = (yield)
        if pattern in line:
            yield line


WORDS = {}


def add_word(word: str, dictionary=WORDS, term=""):
    if len(word) > 0:
        subdict = dictionary.get(word[0])
        if subdict == None:
            dictionary[word[0]] = {}
        term += word[0]
        add_word(word[1:], dictionary[word[0]], term)
    else:
        dictionary["TERM"] = term


def get_words(word: str, dictionary=WORDS):
    tmpdict = dictionary
    for letter in word:
        tmpdict = tmpdict.get(letter)
        if tmpdict == None:
            return []

    result = []
    for elem in tmpdict:
        if elem == "TERM":
            result.append(tmpdict[elem])
        else:
            result.extend(get_words("", tmpdict[elem]))
    return result
