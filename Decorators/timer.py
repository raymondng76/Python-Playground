# timer example used with decorators

import time

def timer(func):
    def wrapper(* args, **kwargs):
        st = time.time()
        results = func(*args, **kwargs)
        tt = time.time() - st
        print(f'{func.__name__} took {str(tt)} second(s).')
        return results
    return wrapper

@timer
def sleep_secs(n):
    time.sleep(n)

if __name__ == '__main__':
    sleep_secs(2)
