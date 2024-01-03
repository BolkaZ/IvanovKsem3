import random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

# Пример использования:

# Список с дубликатами
data_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_iterator = Unique(data_list)

# Выводит только уникальные элементы
for item in unique_iterator:
    print(item)

# Генератор с дубликатами
def gen_random(count, start, end):
    for _ in range(count):
        yield random.randint(start, end)

data_gen = gen_random(10, 1, 3)
unique_iterator_gen = Unique(data_gen)

# Выводит только уникальные элементы
for item in unique_iterator_gen:
    print(item)

# Список строк с дубликатами (учитывая регистр)
data_strings = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_iterator_case_sensitive = Unique(data_strings)

# Выводит только уникальные элементы с учетом регистра
for item in unique_iterator_case_sensitive:
    print(item)

# Список строк с дубликатами (игнорируя регистр)
data_strings_ignore_case = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_iterator_ignore_case = Unique(data_strings_ignore_case, ignore_case=True)

# Выводит только уникальные элементы, игнорируя регистр
for item in unique_iterator_ignore_case:
    print(item)
