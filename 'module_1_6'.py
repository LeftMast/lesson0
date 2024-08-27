my_dict = {"Nikita": 29, "albina": 32, "elvin": 5, "busia": 10}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["albina"]}')
print(f'Not existing value: {my_dict.get("Otis")}')
my_dict.update({"alex": 9,
                "ben": 25})
print(f'Deleted value: {my_dict.pop("busia")}')
print(f'Modified dictionary: {my_dict}')

# Множество
print('_'*40)
my_set = {29, "Cent", 3.1415, "ть"}
print(f'Set: {my_set}')
my_set.update(["Cent", "RU", 38])
my_set.remove(38)
print(f'Modified set: {my_set}')
