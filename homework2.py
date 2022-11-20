def retry(attempts=5, desired_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args:
                lst, *_ = args
            if kwargs.get('size') is not None:
                kwargs.get('size')
            if isinstance(desired_value, int):
                for i in range(attempts):
                    n = func(*args, **kwargs)
                    if n == desired_value:
                        return n
            elif isinstance(desired_value, list):
                result = []
                for i in range(attempts):
                    n = func(*args, **kwargs)
                    result.append(n)
                return result
            return 'failure'
        return wrapper

    return decorator


def draw_square(n, s, f):
    r = s * n
    if not f:
        m = s + " " * (n - 2) + s
    else:
        m = r
    print(r)
    for i in range(n - 2):
        print(m)
    print(r)


draw_square(5, "#", True)
print("")
draw_square(5, "*", False)
