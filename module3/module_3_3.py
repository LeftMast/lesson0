# 1-ая часть.
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# 2-ая часть.
values_list = [3.14, 'str', [5, 6, 7]]
values_dict = {'a': 23, 'b': 'dict', 'c': (4, 3, 2)}
print('-'*20)
print_params(*values_list)
print_params(**values_dict)

# 3-тья часть.
values_list_2 =[54.32, 'Строка' ]
print('-'*20)
print(*values_list_2, 42)