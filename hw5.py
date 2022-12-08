WORDS = {}


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


def add_word(a: str):
    dict2 = {i: a for i in a}
    return dict2


print(add_word('qwerty'))
