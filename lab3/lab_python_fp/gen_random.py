import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

# Пример использования:
random_numbers = gen_random(5, 1, 3)

for number in random_numbers:
    print(number)
