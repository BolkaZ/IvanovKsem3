def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            # Если передано только одно поле, выдаем его значение
            field_name = args[0]
            value = item.get(field_name)
            if value is not None:
                yield value
        else:
            # Если передано несколько полей, формируем словарь с заполненными значениями
            filtered_item = {field: item.get(field) for field in args if item.get(field) is not None}
            if filtered_item:
                yield filtered_item


# Пример использования:
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

# Выдаем значения полей 'title'
for value in field(goods, 'title'):
    print(value)

# Выдаем словари с заполненными значениями полей 'title' и 'price'
for item in field(goods, 'title', 'price'):
    print(item)
