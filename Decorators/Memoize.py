# Memoize example which stores results for fast look ups
import time

def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if (args, kwargs) not in cache:
            cache[(args, kwargs)] = func(*args, **kwargs)
        return cache[(args, kwargs)]
    return wrapper

@memoize
def sleep_add_func(a, b):
    print(f'sleeping...')
    time.sleep(5)
    return a + b

if __name__ == '__main__':
    print(sleep_add_func(1, 5)) # output shows that the lines within sleep_add_func is called

    ##########
    # sleeping...
    # 6
    ##########

    print(sleep_add_func(1, 5)) # output shows the results are immediately returned without executing the lines

    ##########
    # 6
    ##########