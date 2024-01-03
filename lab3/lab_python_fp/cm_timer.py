import time

# на основе класса

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"time: {elapsed_time}")

# Пример использования:

from time import sleep

with cm_timer_1():
    sleep(5.5)



# библиотека contextlib

from contextlib import contextmanager
import time

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"time: {elapsed_time}")

# Пример использования:

from time import sleep

with cm_timer_2():
    sleep(5.5)
