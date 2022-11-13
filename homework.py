def largest_number(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        if b > a:
            return b
        return None
    return None


def less_number(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        if a < b < c:
            return a
        if b < a < c:
            return b
        if c < a < b:
            return c
        return None
    return None


def absolute_value(a):
    if isinstance(a, (int, float)):
        return max(-a, a)
    return None


def sum_of_numbers(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        print(a + b)
    return None


def sign_of_number(c):
    if isinstance(c, (int, float)):
        if c > 0:
            print("Positive number")
        if c == 0:
            print("Zero")
        if c < 0:
            print("Negative number")
    return None
