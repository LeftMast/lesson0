first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_) for str_ in first_strings if len(str_) >= 5]
second_result = [(first_str, second_str) for first_str in first_strings
                 for second_str in second_strings if len(first_str) == len(second_str)]
third_result = {str_: len(str_) for str_ in first_strings + second_strings if not len(str_) % 2}

print(first_result)
print(second_result)
print(third_result)