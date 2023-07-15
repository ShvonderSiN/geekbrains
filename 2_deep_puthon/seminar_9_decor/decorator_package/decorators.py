import csv
import json
from functools import wraps

__all__ = ['save_to_json', 'decor_root']

def save_to_json(dest: str) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            data = {
                'args': args,
                'kwargs': kwargs,
                'result': result
            }

            with open(dest, 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.write('\n')

            return result

        return wrapper

    return decorator


def decor_root(src: str) -> callable:
    with open(src, 'r') as file:
        reader = list(csv.reader(file))

    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for row in reader:
                a, b, c = map(int, row)
                root = func(a, b, c)
                print(f"Корень для {a}, {b}, {c} = {root}")
            if args or kwargs:
                return func(*args, **kwargs)

        return wrapper

    return decor
