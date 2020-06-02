# tutaj wpisz swoje imię i nazwisko

import time
import random
from datetime import datetime

def timer(function):
    t1 = datetime.now()
    function()
    t2 = datetime.now()
    t3 = t2 - t1
    print(f'Czas wykonania: {t3}')

def example_function():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 0.1))
    print()


if __name__ == '__main__':
    timer(example_function)
