my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    number_from_my_list = my_list[index]
    index += 1
    if number_from_my_list == 0:
        continue
    elif number_from_my_list < 0:
        break
    print(number_from_my_list)
