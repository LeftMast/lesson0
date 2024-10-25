def is_int(x):
    return isinstance(x, int)

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            results.update({func.__name__: func(int_list)})
        except TypeError:
            int_list = list(filter(is_int, int_list))
            results.update({func.__name__: func(int_list)})
        except ValueError:
            return f'Список не должен быть пустым: {int_list}\n'

    return results

print(apply_all_func([6, 20, 15, 'e', 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
