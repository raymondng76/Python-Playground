import time


def timer(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        results = func(*args, **kwargs)
        tt = time.time() - st
        print(f"{func.__name__} took {tt} second(s).")
        return results

    return wrapper
