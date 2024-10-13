info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    count = 1
    for str_ in strings:
        key = (count, file.tell())
        count += 1
        strings_positions.update({key: str_})
        file.write(f'{str_}\n')
    file.close()
    return strings_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)