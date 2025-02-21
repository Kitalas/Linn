#exp2
import time

def time_decorator(func):
    def wrapper(*args, *kwargs):
        start_time = time.time()
        result = func(*args, *kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")
        return result
    return wrapper

#exp3
def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

cache = {}
def fibonacci_with_cache(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)
    return cache[n]

from functools import lru_cache

@lru_cache(maxsize=10)
def fibonacci_lru_10(n):
    if n <= 1:
        return n
    return fibonacci_lru_10(n - 1) + fibonacci_lru_10(n - 2)

@lru_cache(maxsize=16)
def fibonacci_lru_16(n):
    if n <= 1:
        return n
    return fibonacci_lru_16(n - 1) + fibonacci_lru_16(n - 2)

for i in range(25):
    print(fibonacci_no_cache(i), fibonacci_with_cache(i), fibonacci_lru_10(i), fibonacci_lru_16(i))

#exp5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_odds = [x*2 for x in numbers if x % 2 != 0]

#exp6
def even_decorator(gen):
    def wrapper():
        for num in gen():
            if num % 2 == 0:
                yield num
    return wrapper

@even_decorator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#exp7
def multiply(a, b):
    return a * b

from functools import partial

curried_multiply = lambda x: lambda y: multiply(x, y)
partially_applied_2 = partial(multiply, 2)
partially_applied_3 = partial(multiply, 3)
