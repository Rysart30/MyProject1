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


def draw_square(n):
    if n == 1:
        print('*')
    if n > 1:
        r = '*' * n
        m = '*' + " " * (n - 2) + '*'
        print(r)
        for i in range(n - 2):
            print(m)
        print(r)
